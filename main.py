#################################
##        Begin Imports        ##
#################################
import re
import io
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

def main():
    mcmasFile = open("examples/simple_card_game.ispl", "r", encoding="utf-8")
    mcmasRaw = mcmasFile.read()
    mcmasFile.close()

    varsAndValues, agents, goals = parseMCMASFile(mcmasRaw)

#################################
##         End Functions       ##
#################################

if __name__ == "__main__":
    main()