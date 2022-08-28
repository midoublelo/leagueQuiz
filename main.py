import cassiopeia as cass
import random

cass.set_riot_api_key("ENTER KEY HERE")

def quiz():
    champList = cass.Champions(region="EUW")
    chosenChamp = random.choice(champList)
    chosenAbility = random.choice(["Passive", "Q", "W", "E", "R"])
    print(f"What is {chosenChamp.name}'s {chosenAbility}?")
    questionAnswer = ""
    
    champAbilities = []
    for spell in chosenChamp.spells:
        champAbilities.append(spell.name)
    #print(champAbilities)
    
    if chosenAbility == "Passive":
        questionAnswer = chosenChamp.passive.name
    elif chosenAbility == "Q":
        questionAnswer = champAbilities[0]
    elif chosenAbility == "W":
        questionAnswer = champAbilities[1]
    elif chosenAbility == "E":
        questionAnswer = champAbilities[2]
    elif chosenAbility == "R":
        questionAnswer = champAbilities[3]
    #print(questionAnswer)
    inputAnswer = input("Enter: ")
    if inputAnswer.lower() == questionAnswer.lower():
        print("Correct")
    else:
        print(f"Wrong it was {questionAnswer}")
    quiz()
quiz()
