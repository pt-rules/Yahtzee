import random

class Die:
    value = 0
    def __init__(self):
        pass

    def roll(self):
       self.value = random.randint(1,6)
