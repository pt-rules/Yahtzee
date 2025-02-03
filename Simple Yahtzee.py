import random
import csv
from die import Die
from scorecard import Scorecard


human = True


def tally_scoring(scorecard, dice_set, dice_count):
    print()


def count_values(dice_set, v):
    result = 0
    for d in dice_set:
        if d.value == v:
            result += 1
    return result

def find_best_category(set, set0, set1):
    max_value = -1
    best_category = "invalid"
    for i in range(0, 10):
        if i == 0:
            category = "ones"
            value = scorecard.add_score(category, set, set1, False)
            if (value > max_value):
                max_value = value
                best_category = "ones"
        if i == 1:
            category = "twos"
            value = scorecard.add_score(category, set, set1, False)
            if (value > max_value):
                max_value = value
                best_category = "twos"
        if i == 2:
            category = "threes"
            value = scorecard.add_score(category, set, set1, False)
            if value > max_value:
                max_value = value
                best_category = "threes"
        if i == 3:
            category = "fours"
            value = scorecard.add_score(category, set, set1, False)
            if value > max_value:
                max_value = value
                best_category = "fours"
        if i == 4:
            category = "fives"
            value = scorecard.add_score(category, set, set1, False)
            if value > max_value:
                max_value = value
                best_category = "fives"
        if i == 5:
            category = "sixes"
            value = scorecard.add_score(category, set, set1, False)
            if value > max_value:
                max_value = value
                best_category = "sixes"
        if i == 6:
            category = "yahtzee"
            value = scorecard.add_score(category, set, set1, False)
            print("yahtzee value")
            print(value)
            if value > max_value:
                max_value = value
                best_category = "yahtzee"
        if i == 7:
            category = "full house"
            value = scorecard.add_score(category, set, set1, False)
            if value > max_value:
                max_value = value
                best_category = "full house"
        if i == 8:
            category = "three of a kind"
            value = scorecard.add_score(category, set, set1, False)
            if value > max_value:
                max_value = value
                best_category = "three of a kind"
        if i == 9:
            category = "four of a kind"
            value = scorecard.add_score(category, set, set1, False)
            if value > max_value:
                max_value = value
                best_category = "four of a kind"
    return best_category
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


def print_set(set0):
    print(f" Dice 1: {set0[0].value}\n Dice 2: {set0[1].value}\n Dice 3: {set0[2].value}\n Dice 4: {set0[3].value}\n Dice 5: {set0[4].value}\n")

def first_reroll(dice_set, human):
    if human == True:
        print_set(dice_set)
        f = -1
        while f < 0:
            f = 0
            reroll = input("Which dice would you like to reroll")
            dice_list = reroll.split()
            #  print(dice_list)
            for d in dice_list:
                if not (d in ['1','2','3','4','5']):
                    f = -1
        return dice_list
    else:
        reroll = []
        return reroll
    
def second_reroll(dice_set, human):
    if human == True:
        print_set(dice_set)
        f = -1
        while f < 0:
            f = 0
            reroll = input("Which dice would you like to reroll")
            dice_list = reroll.split()
            for d in dice_list:
                if not (d in ['1','2','3','4','5']):
                    f = -1
        return dice_list
    else:
        reroll = []
        return reroll
        
def pick_category(set0, set_count, scorecard, human):
    f = -1
    while f < 0:
        if human == True:
            scoring = input("Where would you like to score this? ")
        else:
            scoring = find_best_category(set0, scorecard, set_count)
        f = scorecard.add_score(scoring, set0, set_count, True)
        ## print(f"Category {scoring} Score {f}")

# roll 5 dice

for i in range (0, 25):
    set0 = []
    scorecard = Scorecard()
    count = 0
    for i in range(0,5):
        dice = Die()
        set0.append(dice)
    # play 10 rounds
    for i in range (0, 10):

        # roll all 5 dice
        for d in set0:  
            d.roll()

        # Make the first reroll decision
        x = first_reroll(set0, human)
        for i in x:
            set0[int(i)-1].roll()

        # print_set(set0)
        
        # Make the second reroll decision
        x = second_reroll(set0, human)
        for i in x:  
            set0[int(i)-1].roll()


        # Create a set of counts
        set_count = count_dice(set0)
        scorecard.show_score()

        # Make the scoring decision
        pick_category(set0, set_count, scorecard, human)

        if human == True:
            scorecard.show_score()
            filename = "human_scores.csv"
        else:
            filename = "computer_scores.csv"

    # Save result to file
    x = scorecard.print_scorecard()
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(['ones','twos','threes','fours','fives','sixes','yahtzee','full house','three of a kind','four of a kind'])
        writer.writerow(x)    
