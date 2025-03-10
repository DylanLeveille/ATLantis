#################################
##        Begin Imports        ##
#################################
import re
import shutil
import subprocess
import datetime
import sys

from pathlib import Path
from itertools import chain, combinations, product
from networkx.drawing.nx_agraph import read_dot
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

#MCMAS output file name
mcmasOutputFile = "formula1.dot"

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

    initialState = initialState.strip().rsplit(" ", 1)[0].strip() 
    initialState += " and (player1.play=false) and (player2.play=false)" #FIXME: REMOVE! Get from initial state
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

def parseDOTFile( binFolderPath ):
    #Parse the DOT file into a graph
    DOTFilePath = binFolderPath / mcmasOutputFile
    graph = read_dot( DOTFilePath )

    #Extract a source node (a node with no incoming transition)
    #In uniform strategies, there will be more than one source node
    #We can take any as the strategy is unoform in this case
    srcNode = None
    for node in graph.nodes():
        if ( graph.in_degree(node) == 0 ):
            srcNode = node
            break
    
    actions = list()
    currNode = srcNode

    nextNodeIsCurrent = False
    #While currNode has a neighbour
    while( graph.out_degree(currNode) > 0 and not nextNodeIsCurrent ):
        neighbor = list(graph.neighbors(currNode))[0] #Get a neighbor
        print(neighbor)
        print(currNode)

        if neighbor == currNode:
            nextNodeIsCurrent = True
            print("loop stop")
        else:
            #Action label will conatin actions for all agents
            actionLabel = graph[currNode][neighbor].get(0).get('label')
            print(actionLabel)

            #FIXME: We assume agent for which goals must be found is first agent
            action = actionLabel.split(";")[1].strip()
            actions.append(action)

            currNode = neighbor

    return actions

def findStrategy( mcmasCopy ):
    #Setup before running MCMAS
    binFolderPath = createBinFolder()
    writeMCMASFile(binFolderPath, mcmasCopy)

    #Run MCMAS for uniform strategy
    terminalResult = subprocess.run(uniformStrategyCommand, cwd=binFolderPath, capture_output=True, text=True)

    startegyExists = False
    print("Trying uniform startegy...")
    print(nonUniformStrategyCommand)
    print(terminalResult.stdout)
    if "TRUE in the model" in terminalResult.stdout: #Uniform strategy exists!
        print("Uniform!")
        startegyExists = True
    else: 
        print("No Uniform strategy...")
        print(nonUniformStrategyCommand)
        #Run MCMAS for non-uniform strategy
        terminalResult = subprocess.run(nonUniformStrategyCommand, cwd=binFolderPath, capture_output=True, text=True)
        print(terminalResult.stdout)
        if "TRUE in the model" in terminalResult.stdout: #Non-uniform strategy exists!
            print("Non-Uniform!")
            startegyExists = True
        else:
            print("No Strategy!") #Hence, you probably want to avoid that goal with these pre-conditions

    #If we have a strategy, parse the dot file
    if startegyExists:
        actionsPlan = parseDOTFile( binFolderPath )
    else:
        actionsPlan = list()

    print(actionsPlan)

    return actionsPlan

def writeJasonPlan( strategyActions, goal, knownVars, possibleValue, agentName ):
    #currTime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    jasonFileName = agentName + ".as"

    with open(jasonFileName, "a") as jasonFile:
        jasonFile.write("Goal: " + goal + "\n")
        jasonFile.write("Precondition: \n")
        jasonFile.write("Known Vars: ")

        for var in knownVars:
            jasonFile.write(var)
            jasonFile.write(",")
        jasonFile.write("\n")

        jasonFile.write("Values of known vars: ")
        for i in range( len(knownVars) ):
            jasonFile.write(knownVars[i] + "=" + possibleValue[i])
            jasonFile.write(",")
        jasonFile.write("\n")

        jasonFile.write("Postcondition: \n")
        jasonFile.write("ActionsToTake:")
        for action in strategyActions:
            jasonFile.write(action)
            jasonFile.write(",")
        
        jasonFile.write("\n\n\n")


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
                #Set values in MCMAS file
                mcmasCopy = setInitialState( possibleValue, knownVars, unknownVars, varsAndValues, mcmasCopy)
                mcmasCopy = setGoal( goal, mcmasCopy)

                #Find Strategies
                strategyActions = findStrategy( mcmasCopy )

                #Write Jason Plan
                #FIXME: We assume agent for which goals must be found is first agent
                writeJasonPlan( strategyActions, goal, knownVars, possibleValue, agents[0] )
            
            #break # to remove

        #break # to remove

    return None

def main():
    #FIXME: We assume agent for which goals must be found is first agent
    #FIXME: Change input ispl for user-specified
    #FIXME: Specify next goal for the agent for each goal
    #FIXME: Unknown vars combination (for DEL)
    #FIXME: combinations of known vars seems of of order (card2,card1) shows twice, no (card1,card2)
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