import random
from die import Die
from scorecard import Scorecard

def print_scorecard(scorecard):
    x = [scorecard.ones_score,scorecard.twos_score,scorecard.threes_score,scorecard.fours_score,scorecard.fives_score,scorecard.sixes_score, scorecard.yahtzee_score, scorecard.full_house_score,scorecard.three_kind_score,scorecard.four_kind_score]
    print(x)
    return x

set0 = Scorecard()
set = []
for i in range (0, 5):
    die = Die()
    die.roll()
    set.append(die)
def print_set(set0):
    print(f" Dice 1: {set0[0].value}\n Dice 2: {set0[1].value}\n Dice 3: {set0[2].value}\n Dice 4: {set0[3].value}\n Dice 5: {set0[4].value}\n")
def count_values(dice_set, v):
    result = 0
    for d in dice_set:
        if d.value == v:
            result += 1
    return result
def count_dice(set0):
    set_count = []
    set_count.append(count_values(set0,1))
    set_count.append(count_values(set0,2))
    set_count.append(count_values(set0,3))
    set_count.append(count_values(set0,4))
    set_count.append(count_values(set0,5))
    set_count.append(count_values(set0,6))
    print(set_count)
    return set_count
def find_best_category(set, set0, set1):
    max_value = -1
    best_category = "invalid"
    for i in range(0, 9):
        if i == 0:
            category = "ones"
            value = set0.add_score(category, set, set1, False)
            if (value > max_value):
                max_value = value
                best_category = "ones"
        if i == 1:
            category = "twos"
            value = set0.add_score(category, set, set1, False)
            if (value > max_value):
                max_value = value
                best_category = "twos"
        if i == 2:
            category = "threes"
            value = set0.add_score(category, set, set1, False)
            if value > max_value:
                max_value = value
                best_category = "threes"
        if i == 3:
            category = "fours"
            value = set0.add_score(category, set, set1, False)
            if value > max_value:
                max_value = value
                best_category = "fours"
        if i == 4:
            category = "fives"
            value = set0.add_score(category, set, set1, False)
            if value > max_value:
                max_value = value
                best_category = "fives"
        if i == 5:
            category = "sixes"
            value = set0.add_score(category, set, set1, False)
            if value > max_value:
                max_value = value
                best_category = "sixes"
        if i == 6:
            category = "yahtzee"
            value = set0.add_score(category, set, set1, False)
            print("yahtzee value")
            print(value)
            if value > max_value:
                max_value = value
                best_category = "yahtzee"
        if i == 7:
            category = "full house"
            value = set0.add_score(category, set, set1, False)
            if value > max_value:
                max_value = value
                best_category = "full house"
        if i == 8:
            category = "three of a kind"
            value = set0.add_score(category, set, set1, False)
            if value > max_value:
                max_value = value
                best_category = "three of a kind"
        if i == 9:
            category = "four of a kind"
            value = set0.add_score(category, set, set1, False)
            if value > max_value:
                max_value = value
                best_category = "four of a kind"
    return best_category

set1 = count_dice(set)
print(set1)
category_choice = find_best_category(set, set0, set1)
        

print_set(set)
print(category_choice)
set0.add_score(category_choice, set, set1, True)
print_scorecard(set0)

set = []
for i in range (0, 5):
    die = Die()
    die.roll()
    set.append(die)
    
set1 = count_dice(set)
category_choice = find_best_category(set, set0, set1)
print_set(set)
set0.add_score(category_choice, set, set1, True)
print_scorecard(set0)

set = []
for i in range (0, 5):
    die = Die()
    die.roll()
    set.append(die)
set1 = count_dice(set)
category_choice = find_best_category(set, set0, set1)
print_set(set)
set0.add_score(category_choice, set, set1, True)
print_scorecard(set0)