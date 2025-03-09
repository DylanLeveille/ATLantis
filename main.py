#################################
##        Begin Imports        ##
#################################
import re
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
    specialPrint(agent)
    # Define the new Lobsvars values for player1
    new_lobsvars = "{card1=a, card2=k}" #account for spaces after Agent keyword

    # Regular expression to match the Lobsvars block for player1 and replace it
    pattern = r"(Agent player1\s+Lobsvars=)\{.*?\};"
    pattern = rf"(Agent {re.escape(agent)}\s+Lobsvars=)\{{.*?\}};"
    replacement = r"\1" + new_lobsvars + ";"

    # Perform the replacement
    modified_data = re.sub(pattern, replacement, mcmasCopy, flags=re.DOTALL)

    return modified_data

    # Print the modified data
    #print(modified_data)

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
            varsAndValues[var.strip()] = value.strip()
    
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
                print(mcmasCopy)
                
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