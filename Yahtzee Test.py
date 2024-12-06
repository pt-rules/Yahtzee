import random
class Die:
    value = 0
    def __init__(self):
        pass

    def roll(self):
        self.value = random.randint(1,6)
number = 0
total = 0
while number < 1000:    
    count = 0
    rolls = 0
    while count == 0:
        dice1 = Die()
        dice1.roll()
        dice2 = Die()
        dice2.roll()
        dice3 = Die()
        dice3.roll()
        dice4 = Die()
        dice4.roll()
        dice5 = Die()
        dice5.roll()
        set1 = []

        #First Roll
        set1.append(dice1.value)
        set1.append(dice2.value)
        set1.append(dice3.value)
        set1.append(dice4.value)
        set1.append(dice5.value)
        count_ones = set1.count(1)
        if count_ones == 5:
            print("Yahtzee")
            count += 1
        count_twos = set1.count(2)
        if count_twos == 5:
            print("Yahtzee")
            count += 1
        count_threes = set1.count(3)
        if count_threes == 5:
            print("Yahtzee")
            count += 1
        count_fours = set1.count(4)
        if count_fours == 5:
            print("Yahtzee")
            count += 1
        count_fives = set1.count(5)
        if count_fives == 5:
            print("Yahtzee")
            count += 1
        count_sixes = set1.count(6)
        if count_sixes == 5:
            print("Yahtzee")
            count += 1
        rolls += 1
    print(rolls)
    total += rolls
    number += 1

total = total / number
print(total)