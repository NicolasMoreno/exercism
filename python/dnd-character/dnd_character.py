import random
import math
# from functools import reduce

class Character:
    # strength, dexterity, constitution, intelligence, wisdom and charisma
    
    def __init__(self):
        self.strength = self.rollCharacterAbilityDice()
        self.dexterity = self.rollCharacterAbilityDice()
        self.constitution = self.rollCharacterAbilityDice()
        self.intelligence = self.rollCharacterAbilityDice()
        self.wisdom = self.rollCharacterAbilityDice()
        self.charisma = self.rollCharacterAbilityDice()
        self.hitpoints = self.setHitpoints()

    def rollCharacterAbilityDice(self):
        rolledDice = []
        for x in range(0,3):
            rolledDice.append(self.rollDice())
        rolledDice.sort()
        points = sum(rolledDice[1:4])
        return points

    def rollDice(self):
        return random.randint(1,6)

    def ability(self):
        return self.strength

    def setHitpoints(self):
        return 10 + modifier(self.constitution)


def modifier(baseConstitution):
    return math.floor((baseConstitution - 10)/2)