import random
set1 = []
score = 0
ones_score = -1
twos_score = -1
threes_score = -1
fours_score = -1
fives_score = -1
sixes_score = -1
small_straight = -1
large_straight = -1
class Scorecard:
    score = 0
    ones_score = -1
    twos_score = -1
    threes_score = -1
    fours_score = -1
    fives_score = -1
    sixes_score = -1
    yahtzee = -1
    arrays = []
    def __init__(self):
        pass
    def add_points(self, set1):
        self.score += set1
    def add_array(self, set1, arrays):
        arrays.append(set1)
        return arrays
    def add_score(self, x, ones_score, score):
        if ones_score < 0:
            ones_score += x
            score += ones_score 
            return score
        else:
            pass

class Die:
    value = 0
    def __init__(self):
        pass

    def roll(self):
       self.value = random.randint(1,6)
def not_equal(var):
    return var == exclude
#Printing the best number
def check_best(best_option, count_ones, count_twos, count_threes, count_fours, count_fives, count_sixes):
    if best_option == "Ones":
        exclude = 1
        total = exclude * count_ones
        return exclude
    if best_option == "Twos":
        exclude = 2
        total = exclude * count_twos
        return exclude
    if best_option == "Threes":
        exclude = 3
        total = exclude * count_threes
        return exclude
    if best_option == "Fours":
        exclude = 4
        total = exclude * count_fours
        return exclude
    if best_option == "Fives":
        exclude = 5
        total = exclude * count_fives
        return exclude
    if best_option == "Sixes":
        exclude = 6
        total = exclude * count_sixes

        return exclude
#Checking the dice
def check_dice(dice1,exclude):
    if dice1.value != exclude:
      dice1.roll()
      set1.append(dice1.value)

    else:
        pass
total = 0
stored_sets = []
def load_set(set, set1): 
    set.add_array(set1, stored_sets)
    return set
yahtzee_total = 0
count = 0
set = Scorecard()

for i in range(1,10):
    count += 1
    set0 = []
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
    set0.append(dice1.value)
    set0.append(dice2.value)
    set0.append(dice3.value)
    set0.append(dice4.value)
    set0.append(dice5.value)

    #Checking the numbers
    count_ones = set0.count(1)
    count_twos = set0.count(2)
    count_threes = set0.count(3)
    count_fours = set0.count(4)
    count_fives = set0.count(5)
    count_sixes = set0.count(6)
    set2 = {'Ones': count_ones, 'Twos': count_twos, 'Threes': count_threes, 'Fours': count_fours, 'Fives': count_fives, 'Sixes': count_sixes}
    best_option = max(set2, key=set2.get)

    exclude = check_best(best_option, count_ones, count_twos, count_threes, count_fours, count_fives, count_sixes)
    set1 = list(filter(not_equal, set1))
    #Rerolling dice
    check_dice(dice1,exclude)
    check_dice(dice2,exclude)
    check_dice(dice3,exclude)
    check_dice(dice4,exclude)
    check_dice(dice5,exclude)


    #Counting dice
    count_ones = set0.count(1)
    count_twos = set0.count(2)
    count_threes = set0.count(3)
    count_fours = set0.count(4)
    count_fives = set0.count(5)
    count_sixes = set0.count(6)
    set2 = {'Ones': count_ones, 'Twos': count_twos, 'Threes': count_threes, 'Fours': count_fours, 'Fives': count_fives, 'Sixes': count_sixes}
    best_option = max(set2, key=set2.get)
    exclude = check_best(best_option, count_ones, count_twos, count_threes, count_fours, count_fives, count_sixes)
    set1 = list(filter(not_equal, set1))
    check_dice(dice1,exclude)
    check_dice(dice2,exclude)
    check_dice(dice3,exclude)
    check_dice(dice4,exclude)
    check_dice(dice5,exclude)
    count_ones = set1.count(1)
    if count_ones == 5:
        print("Yahtzee") 
        yahtzee_total += 1
    count_twos = set1.count(2)
    if count_twos == 5:
        print("Yahtzee")
        yahtzee_total += 1
    count_threes = set1.count(3)
    if count_threes == 5:
        print("Yahtzee")
        yahtzee_total += 1
    count_fours = set1.count(4)
    if count_fours == 5:
        print("Yahtzee")
        yahtzee_total += 1
    count_fives = set1.count(5)
    if count_fives == 5:
        print("Yahtzee")
        yahtzee_total += 1
    count_sixes = set1.count(6)
    if count_sixes == 5:
        print("Yahtzee")
        yahtzee_total += 1
    set2 = {'Ones': count_ones, 'Twos': count_twos, 'Threes': count_threes, 'Fours': count_fours, 'Fives': count_fives, 'Sixes': count_sixes}
    best_option = max(set2, key=set2.get)
    exclude = check_best(best_option, count_ones, count_twos, count_threes, count_fours, count_fives, count_sixes)
    set = load_set(set, set0)
    score = set.add_score(exclude, ones_score, score)
    print(set0)
print(total)
print(set.score)