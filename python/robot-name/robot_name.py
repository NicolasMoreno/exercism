import string
import random

class Robot(object):
    def __init__(self):
        self.name = self.generateRandomName()
    
    def generateRandomName(self):
        random.seed(a=None)
        uppStringPart = random.choices(string.ascii_uppercase, k=2)
        digitPart = random.choices(string.digits, k=3)
        return ''.join(uppStringPart) + ''.join(digitPart)

    def reset(self):
        self.name = self.generateRandomName()

