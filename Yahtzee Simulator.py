import random
set1 = []
class Die:
    value = 0
    def __init__(self):
        pass

    def roll(self):
        self.value = random.randint(1,6)

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

#First Roll
set1.append(dice1.value)
set1.append(dice2.value)
set1.append(dice3.value)
set1.append(dice4.value)
set1.append(dice5.value)
print(set1)

#Checking the numbers
count_ones = set1.count(1)
count_twos = set1.count(2)
count_threes = set1.count(3)
count_fours = set1.count(4)
count_fives = set1.count(5)
count_sixes = set1.count(6)
set2 = {'Ones': count_ones, 'Twos': count_twos, 'Threes': count_threes, 'Fours': count_fours, 'Fives': count_fives, 'Sixes': count_sixes}
best_option = max(set2, key=set2.get)
#Checking the dice
def check_dice(dice1,exclude):
    if dice1.value != exclude:
      dice1.roll()
      set1.append(dice1.value)

    else:
        pass

#Printing the best number
def check_best(best_option, count_ones, count_twos, count_threes, count_fours, count_fives, count_sixes):
    if best_option == "Ones":
        print()
        print(count_ones)
        print(best_option)
        exclude = 1
        total = exclude * count_ones
        print(total)
        return exclude
    if best_option == "Twos":
        print()
        print(count_twos)
        print(best_option)
        exclude = 2
        total = exclude * count_twos
        print(total)
        return exclude
    if best_option == "Threes":
        print(count_threes)
        print(best_option)
        exclude = 3
        total = exclude * count_threes
        print(total)
        return exclude
    if best_option == "Fours":
        print()
        print(count_fours)
        print(best_option)
        exclude = 4
        total = exclude * count_fours
        print(total)
        return exclude
    if best_option == "Fives":
        print()
        print(count_fives)
        print(best_option)
        exclude = 5
        total = exclude * count_fives
        print(total)
        return exclude
    if best_option == "Sixes":
        print()
        print(count_sixes)
        print(best_option)
        exclude = 6
        total = exclude * count_sixes
        print(total)
        return exclude
exclude = check_best(best_option, count_ones, count_twos, count_threes, count_fours, count_fives, count_sixes)
def not_equal(var):
    return var == exclude
set1 = list(filter(not_equal, set1))
#Rerolling dice
check_dice(dice1,exclude)
check_dice(dice2,exclude)
check_dice(dice3,exclude)
check_dice(dice4,exclude)
check_dice(dice5,exclude)


#Counting dice
count_ones = set1.count(1)
count_twos = set1.count(2)
count_threes = set1.count(3)
count_fours = set1.count(4)
count_fives = set1.count(5)
count_sixes = set1.count(6)
print(set1)
set2 = {'Ones': count_ones, 'Twos': count_twos, 'Threes': count_threes, 'Fours': count_fours, 'Fives': count_fives, 'Sixes': count_sixes}
best_option = max(set2, key=set2.get)
exclude = check_best(best_option, count_ones, count_twos, count_threes, count_fours, count_fives, count_sixes)

check_dice(dice1,exclude)
check_dice(dice2,exclude)
check_dice(dice3,exclude)
check_dice(dice4,exclude)
check_dice(dice5,exclude)