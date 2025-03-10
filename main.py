#################################
##        Begin Imports        ##
#################################
import re
import shutil
import subprocess

from pathlib import Path
from itertools import chain, combinations, product
#################################
##         End Imports         ##
#################################

#################################
##        Begin Globals        ##
#################################

#Environment Variables
environmentVarsPattern = r"Agent Environment[\s\S]*?Vars:\n([\s\S]*?)end Vars"
varAndValuesPattern = r"\s+(\w+)\s*:\s*(\{[^}]+\});"

#Goals
goalsPattern = r"^Formulae\s*\n([\s\S]*?)^end Formulae"

#bin folder path
binFolder = "bin"

#MCMAS input file name
mcmasInputFile = "input.ispl"

#MCMAS uniform and non-uniform strategy commands
uniformStrategyCommand = ["../mcmas/mcmas-linux64-1.3.0", "-c", "3", "-uniform", mcmasInputFile ]
nonUniformStrategyCommand = ["../mcmas/mcmas-linux64-1.3.0", "-c", "3", mcmasInputFile ]

#################################
##         End Globals         ##
#################################

#################################
##        Begin Functions      ##
#################################

def specialPrint(msg):
    print("***************************************")
    print(msg)
    print("***************************************\n")

def powerset(iterable):
    s = list(iterable)
    return set(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

def setLobsvarForAgent( agent, agentVariables, mcmasCopy ):
    lobsvars = "{" 

    for var in agentVariables:
        lobsvars += ( var + "," )

    if ( len( agentVariables ) > 0 ):
        lobsvars = lobsvars[:-1]

    lobsvars += "}"

    #Pattern to replace Lobsvar with
    pattern = rf"(Agent\s+{re.escape(agent)}\s+Lobsvars=)\{{.*?\}};"
    replacement = r"\1" + lobsvars + ";"

    #Replace Lobsvar for the agent
    mcmasNew = re.sub(pattern, replacement, mcmasCopy, flags=re.DOTALL)

    return mcmasNew

def setInitialState( possibleValue, knownVars, unknownVars, varsAndValues, mcmasCopy ):
    initialState = ""
    for i in range( len(knownVars) ):
        initialState += "( Environment." + knownVars[i] + "=" + possibleValue[i] + " )"
        initialState += " and "

    for i in range( len(unknownVars) ):
        initialState += "( " 
        unknownVar = unknownVars[i]

        valuesForUnknownVar = varsAndValues[unknownVar]
        for j in range( len(valuesForUnknownVar) ):
            initialState+= "Environment." + unknownVar + "=" + valuesForUnknownVar[j]

            if j != ( len(valuesForUnknownVar) - 1 ):
                initialState += " or "

        initialState += ") "

        initialState += " and "

    initialState = initialState.strip().rsplit(" ", 1)[0].strip() #fix me
    initialState += ";"

    #replace with initial state computed
    pattern = r"InitStates.*?end InitStates"
    replacement = "InitStates\n\n\t" + initialState + "\n\nend InitStates"

    mcmasNew = re.sub(pattern, replacement, mcmasCopy, flags=re.DOTALL)

    return mcmasNew

def setGoal( goal, mcmasCopy):
    pattern = r"Formulae.*?end Formulae"
    replacement = "Formulae\n\n\t" + goal + "\n\nend Formulae"

    mcmasNew = re.sub(pattern, replacement, mcmasCopy, flags=re.DOTALL)

    return mcmasNew

def createBinFolder():
    #Create the bin folder to store MCMAS results
    currFolderPath = Path(".")
    binFolderPath = currFolderPath / binFolder

    #Wipe out folder if it already exists
    if binFolderPath.exists():
        shutil.rmtree(binFolderPath)

    #create new bin path
    binFolderPath.mkdir()

    return binFolderPath

def writeMCMASFile(binFolderPath, mcmasCopy):
    #Write the MCMAS file
    filePath = binFolderPath / mcmasInputFile
    filePath.write_text(mcmasCopy)

def findStrategy( mcmasCopy ):
    #Setup before running MCMAS
    binFolderPath = createBinFolder()
    writeMCMASFile(binFolderPath, mcmasCopy)

    #Run MCMAS for uniform strategy
    terminalResult = subprocess.run(uniformStrategyCommand, cwd=binFolderPath, capture_output=True, text=True)

    if "TRUE in the model" in terminalResult.stdout: #Uniform strategy exists!
        print("Uniform!")
    else: 
        #Run MCMAS for non-uniform strategy
        terminalResult = subprocess.run(nonUniformStrategyCommand, cwd=binFolderPath, capture_output=True, text=True)

        if "TRUE in the model" in terminalResult.stdout: #Non-uniform strategy exists!
            print("Non-Uniform!")
        else:
            print("No Strategy!")

    return None

def parseMCMASFile(mcmasRaw):
    varsAndValues = dict()
    agents = list()
    goals = list()
    
    #Extract environment variables and their values
    match = re.search(environmentVarsPattern, mcmasRaw)
    if match:

        #Extract the Vars section
        varsSection = match.group(1)  

        #Extract individual variables and values
        match = re.findall(varAndValuesPattern, varsSection)

        for var, value in match:
            actualValues = list()
            #value is a set of values
            if "{" in value:
                value = value.replace("{", "").replace("}", "")
                for element in value.split(","):
                    actualValues.append(element.strip())

            elif "boolean" in value:
                actualValues.append("true")
                actualValues.append("false")
            
            else: #has form x..y (i.e., integers x to y inclusive)
                integersString = re.findall(r'\d+', value)
                integers = list(map(int, integersString))
                actualValues = list(range( integers[0], integers[1] ))

            varsAndValues[var.strip()] = actualValues
    
    #Extract all Agents, except environement
    for line in mcmasRaw.splitlines():
        if line.startswith("Agent"):
            agent = line.split(" ", 1)[1].strip()

            if agent != "Environment":
                agents.append(agent)

    #Extract all Goals
    match = re.search(goalsPattern, mcmasRaw, re.MULTILINE)

    if match:
        for line in match.group(1).strip().split("\n"):
            if not line.startswith("--"): #ignore commented goals
                goals.append(line.strip())

    print("Environment Variables and Values Detected:")
    print(varsAndValues)
    print("Agents Detected:")
    print(agents)
    print("Goals Detected:")
    print(goals)

    return varsAndValues, agents, goals

def generatePlans(varsAndValues, agents, goals, mcmasRaw):
    plans = list()
    numAgents = len(agents)
    vars = set(varsAndValues.keys())
    
    powersetVars = powerset(vars)
    allAgentVariablePermutations = set(product(powersetVars, repeat=numAgents))

    for goal in goals:
        for agentVariablePermutations in allAgentVariablePermutations:
            mcmasCopy = str(mcmasRaw) #Make a copy of raw text (we modify this copy)

            for i in range(numAgents):
                agentVariables = agentVariablePermutations[i]
                
                mcmasCopy = setLobsvarForAgent( agents[i], agentVariables, mcmasCopy )

                knownVars = set(agentVariablePermutations[0]) 
                unknownVars = vars - knownVars
                
                #fix order of known vars for possible associated values
                knownVars = list(knownVars)
                unknownVars = list(unknownVars)
                possibleValuesElements = list()
                
                for var in knownVars:
                    possibleValuesElements.append( varsAndValues[var] )
                
                possibleValues = list( product(*possibleValuesElements) )

                for possibleValue in possibleValues:
                    
                    mcmasCopy = setInitialState( possibleValue, knownVars, unknownVars, varsAndValues, mcmasCopy)
                    mcmasCopy = setGoal( goal, mcmasCopy)

                    plans.append( findStrategy( mcmasCopy ) )
                
            break # to remove

        break # to remove

    return None

def main():
    # We assume agent for which goals must be found is first agent
    mcmasFile = open("examples/simple_card_game.ispl", "r", encoding="utf-8")
    mcmasRaw = mcmasFile.read()
    mcmasFile.close()

    varsAndValues, agents, goals = parseMCMASFile(mcmasRaw)

    plans = generatePlans(varsAndValues, agents, goals, mcmasRaw)

#################################
##         End Functions       ##
#################################

if __name__ == "__main__":
    main()