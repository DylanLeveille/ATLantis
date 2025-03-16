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

#All Variables
varsPattern = r"Vars:\n([\s\S]*?)end Vars"

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

def powerset(iterable):
    s = list(iterable)
    result = list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    return sorted(result, key=len, reverse=True)

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

def setInitialState( knownPossibleValue, knownVars, unknownPossibleValue, unknownVars, mcmasCopy, fixedInitialState ):
    initialState = fixedInitialState + " "
    for i in range( len(knownVars) ):
        initialState += "( Environment." + knownVars[i] + "=" + knownPossibleValue[i] + " )"
        initialState += " and "

    for i in range( len(unknownVars) ):
        initialState += "( " 
        unknownVar = unknownVars[i]

        valuesForUnknownVar = unknownPossibleValue[i]
        for j in range( len(valuesForUnknownVar) ):
            initialState+= "Environment." + unknownVar + "=" + valuesForUnknownVar[j]

            if j != ( len(valuesForUnknownVar) - 1 ):
                initialState += " or "

        initialState += ")"

        initialState += " and "

    initialState = initialState.strip().rsplit(" ", 1)[0].strip() 
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

    return startegyExists, actionsPlan

def writeJasonPlan( strategyActions, goal, knownVars, knownPossibleValue, unknownVars, unknownPossibleValue, agentName):
    #currTime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    jasonFileName = agentName + ".as"

    with open(jasonFileName, "a") as jasonFile:
        #Write goal
        jasonFile.write("+!" + goal[:-1] + ":")

        #Write pre-conditions
        for  i in range( len(knownVars) ):
            jasonFile.write("\n")
            jasonFile.write("\t")
            jasonFile.write(knownVars[i] + "=" + knownPossibleValue[i])
            if ( len(unknownVars) > 0 or i < len(knownVars) - 1 ):
                jasonFile.write(" &")

        for  i in range( len(unknownVars) ):
            for j in range( len(unknownPossibleValue[i]) ):
                possValue = unknownPossibleValue[i][j]
                jasonFile.write("\n")
                jasonFile.write("\t")
                jasonFile.write("poss(" + unknownVars[i] + "=" + possValue + ")")
                if ( i < len(unknownVars) - 1  or j < len(unknownPossibleValue[i]) - 1 ):
                    jasonFile.write(" &")

        jasonFile.write("\n\t<-")

        jasonFile.write("\n")
        jasonFile.write("\t")
        for i in range(len(strategyActions)):
            jasonFile.write(strategyActions[i])
            if ( len(strategyActions) - 1 ==  ( i - 1 ) ): #last action, put .
                jasonFile.write(".")
            else:
                jasonFile.write(";")
        
        jasonFile.write("\n\n")

def setFixVariables(varsForAgent):
    #Prompt user to fix values for agent variables. This will be used as part of initial state
    print("*** Initial State Configuration ***")
    print("*** Set Agent Variables ***")
    fixedInitialState = ""
    for agent in varsForAgent.keys():
        if agent != "Environment":
            for agentVar in varsForAgent[agent]:
                value = input("Value for " + agent + "." + agentVar + " ?: ")
                fixedInitialState += "(" + agent + "." + agentVar + "=" + value.strip() + ") and "
    print("*** Set Environment Variables ***")     
    shouldFixEnvVariables = input("Should any environment variables be statically set? (y/n): ")
    fixedEnvVariables = list()
    if ( shouldFixEnvVariables.strip() == "y" ):
        fixEnvVariables = input("Which variables? (comma seperated): ")
        for fixedVar in fixEnvVariables.split(","):
            fixedVar = fixedVar.strip()
            fixedEnvVariables.append(fixedVar)
            value = input("Value for Environment." + fixedVar + " ?: ")
            fixedInitialState += " (" + "Environement" + "." + fixedVar + "=" + value.strip() + ") and "

    return fixedInitialState, fixedEnvVariables

def parseMCMASFile(mcmasRaw):
    varsAndValues = dict()
    varsForAgent = dict()
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
    
    #Extract all Agents, except environement. And extract all Vars
    varsSection = False
    agentVariables = list()
    mostRecentAgent = None
    for line in mcmasRaw.splitlines():
        if line.strip().startswith("Agent"):
            agent = line.split(" ", 1)[1].strip()
            mostRecentAgent = agent

            if agent != "Environment":
                agents.append(agent)

        if line.strip().startswith("Vars"):
            varsSection = True

        elif varsSection:
            line = line.strip()
            if line: 
                if line.split(" ")[0].startswith("end"):
                    varsSection = False
                    varsForAgent[mostRecentAgent] = agentVariables
                    agentVariables = list()
                else:
                    var = line.split(":")[0].strip()
                    agentVariables.append(var)
            
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
    print("Variables for Agents")
    print(varsForAgent)
    print("Goals Detected:")
    print(goals)

    return varsAndValues, agents, varsForAgent, goals

def generatePlans(varsAndValues, agents, goals, mcmasRaw, fixedInitialState):
    plans = list()
    idealPlans = dict()
    numAgents = len(agents)
    numPermutations = 1 # Ideally, should be set to numAgents. But MCMAS, does not support knowledge based actions
    vars = list(varsAndValues.keys())
    vars.sort()
    
    powersetVars = powerset(vars) 
    allAgentVariablePermutations = list(product(powersetVars, repeat=numPermutations)) 

    for goal in goals:
        for agentVariablePermutations in allAgentVariablePermutations:
            mcmasCopy = str(mcmasRaw) #Make a copy of raw text (we modify this copy)

            for i in range(numPermutations): #FIXME: We assume agent for which goals must be found is first agent
                agentVariables = agentVariablePermutations[i]
                
                mcmasCopy = setLobsvarForAgent( agents[i], agentVariables, mcmasCopy )

            knownVars = list(agentVariablePermutations[0]) #FIXME: We assume agent for which goals must be found is first agent
            unknownVars = [var for var in vars if var not in knownVars]
            completeCertainty = True if len(unknownVars) == 0 else False 
            
            # A known variable can only possess one possible value
            # An unknown variable can posses any number of possible values 
            knownPossibleValuesElements = list()
            unknownPossibleValuesElements = list()
            
            for var in knownVars:
                knownPossibleValuesElements.append( varsAndValues[var] )
            for var in unknownVars:
                poss = powerset( varsAndValues[var] ) #Careful, this includes empty set which is not true here
                poss = [ s for s in poss if s ]
                unknownPossibleValuesElements.append( poss ) 

            knownPossibleValues = list( product(*knownPossibleValuesElements) ) #possible values for known variables
            unknownPossibleValues = list( product(*unknownPossibleValuesElements) ) #possible values for unknown variables

            for knownPossibleValue in knownPossibleValues: #Example: Card 1 = King and Card 2 = Ace
                for unknownPossibleValue in unknownPossibleValues: #Example: ( poss(Card3 = King) and poss(Card3 = Queen); poss(Card4, King) and poss(Card4, Queen) )
                    
                    # We don't want to apply the algorithm when an unkown variable has only one possible value
                    if not any( len(possValues) == 1 for possValues in unknownPossibleValue ):
                        #Set values in MCMAS file
                        mcmasCopy = setInitialState( knownPossibleValue, knownVars, unknownPossibleValue, unknownVars, mcmasCopy, fixedInitialState )
                        mcmasCopy = setGoal( goal, mcmasCopy)

                        #Find Strategies
                        strategyExists, strategyActions = findStrategy( mcmasCopy )

                        #if complete certainty and goal true, add to idea plans list (complete knowledge strategies)
                        if completeCertainty:
                            if strategyExists:
                                idealPlans[ tuple(knownPossibleValue) ] = strategyActions
                            else:
                                print("random action")
                        #if partial certainty and goal false, loop uncertainty with goodie list until strat. 
                        else:
                            if not strategyExists:
                                #Create all concrete permutations for the possible values of ecah variable
                                permPossibleValues = list( product(*unknownPossibleValue) )
                                
                                #Loop through each possible concrete values for unknown variables. Fetch actions from ideal strategies
                                for permPossibleValue in permPossibleValues:
                                    #construct key for dictionary
                                    dictKey = list()
                                    knownVarIndex = 0
                                    unknownVarIndex = 0
                                    for var in vars: #vars is alphabetically ordered. Hence all other lists are as well
                                        if var in knownVars:
                                            dictKey.append(knownPossibleValue[knownVarIndex])
                                            knownVarIndex += 1
                                        else:
                                            dictKey.append(permPossibleValue[unknownVarIndex])
                                            unknownVarIndex += 1

                                    actualDictKey = tuple(dictKey)
                                    if actualDictKey in idealPlans:
                                        strategyActions = idealPlans[actualDictKey]
                                        strategyExists = True
                                        break #we found a plan, so stop

                        #if we could not find actions to do, means we cannot achieve this goal no matter what we do (no chance of getting goal)            
                        if not strategyExists:
                            print("out of luck")

                        #Write Jason Plan
                        #FIXME: We assume agent for which goals must be found is first agent
                        writeJasonPlan( strategyActions, goal, knownVars, knownPossibleValue, unknownVars, unknownPossibleValue, agents[0] )
                
            #break # to remove

        #break # to remove

    return None

def main():
    #FIXME: We assume agent for which goals must be found is first agent
    #FIXME: Change input ispl for user-specified
    #FIXME: Specify next goal for the agent for each goal
    mcmasFile = open("examples/simple_card_game.ispl", "r", encoding="utf-8")
    mcmasRaw = mcmasFile.read()
    mcmasFile.close()

    varsAndValues, agents, varsForAgent, goals = parseMCMASFile(mcmasRaw)

    fixedInitialState, fixedEnvVariables = setFixVariables(varsForAgent)

    # Remove fixed environment variables from varsAndValues
    for fixedEnvVariable in fixedEnvVariables:
        varsAndValues.pop(fixedEnvVariable)

    plans = generatePlans(varsAndValues, agents, goals, mcmasRaw, fixedInitialState)

#################################
##         End Functions       ##
#################################

if __name__ == "__main__":
    main()