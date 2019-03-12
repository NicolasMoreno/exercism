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

    def rollCharacterAbilityDice(self):
        rolledDice = [self.rollDice(), self.rollDice(), self.rollDice(), self.rollDice()].sort()
        print(rolledDice)
        points = sum(rolledDice[1:4])
        # points = reduce(lambda x,y: x+y, rolledDice[1:4])
        return points

    def rollDice(self):
        return random.randint(1,6)

    def ability(self):
        return self.strength


def modifier(baseConstitution):
    return math.floor((baseConstitution - 10));