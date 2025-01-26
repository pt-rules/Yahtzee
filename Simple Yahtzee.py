import random
import csv
class Scorecard:
    ones_score = -1
    twos_score = -1
    threes_score = -1
    fours_score = -1
    fives_score = -1
    sixes_score = -1
    yahtzee_score = -1
    full_house_score = -1
    three_kind_score = -1
    four_kind_score = -1
    total = 0
    def __init__(self):
        pass
    def add_score(self, category, dice_set, dice_count):
        count = -1
        if category == "ones":
            count = 0
            if self.ones_score < 0:
                self.ones_score = 0
                for d in dice_set:
                    if d.value == 1:
                        print("found a one")
                        self.ones_score += 1
                        self.total += 1
                # self.ones_score += dice_set.count(1)
            else:
              print("invalid - you used ones already")
        if category == "twos":
            count = 0
            if self.twos_score < 0:
                self.twos_score = 0

                for d in dice_set:
                    if d.value == 2:
                        print("found a two")
                        self.twos_score += 2
                        self.total += 2
            else:
                print("invalid - you used twos already") 
        if category == "threes":
            count = 0
            if self.threes_score < 0:
                self.threes_score = 0

                for d in dice_set:
                    if d.value == 3:
                        print("found a three")
                        self.threes_score += 3
                        self.total += 3
            else:
                print("invalid - you used threes already")
        if category == "fours":
            count = 0
            if self.fours_score < 0:
                self.fours_score = 0

                for d in dice_set:
                    if d.value == 4:
                        
                        print("found a four")
                        self.fours_score += 4
                        self.total += 4
            else:
                print("invalid - you used fours already")
        if category == "fives":
            count = 0
            if self.fives_score < 0:
                self.fives_score = 0
                for d in dice_set:
                    if d.value == 5:
                        self.fives_score += 5
                        self.total += 5
            else:
                print("invalid - you used fives already")
        if category == "sixes":
            count = 0
            if self.sixes_score < 0:
                self.sixes_score = 0

                for d in dice_set:
                    if d.value == 6:
                        print("found a six")
                        self.sixes_score += 6
                        self.total += 1
            else:
                print("invalid - you used sixes already")
        if category == "yahtzee":
            if self.yahtzee_score < 0:
                count = 0
                self.yahtzee_score = 0
                if 1 in dice_set:
                    print("H")
                    if 1 in dice_count == 5:
                        self.yahtzee_score += 50
                        self.total += 50
                elif 2 in dice_set:
                    print("H")
                    if 2 in dice_count == 5:
                        self.yahtzee_score += 50
                        self.total += 50
                elif 3 in dice_set:
                    print("H")
                    if 3 in dice_count == 5:
                        self.yahtzee_score += 50
                        self.total += 50
                elif 4 in dice_set:
                    print("H")
                    if 4 in dice_count == 5:
                        self.yahtzee_score += 50
                        self.total += 50
                elif 5 in dice_set:
                    print("H")
                    if 5 in dice_count == 5:
                        self.yahtzee_score += 50
                        self.total += 50
                elif 6 in dice_set:
                    print("H")
                    if 6 in dice_count == 5:
                        self.yahtzee_score += 50
                        self.total += 50
        if category == "full house":
            if self.full_house_score < 0:
                count = 0
                self.full_house_score = 0
                if 2 in dice_count:
                    if 3 in dice_count:
                        self.full_house_score += 25
                        self.total += 25

        if category == "three of a kind":
            if self.three_kind_score < 0:
                count = 0
                self.three_kind_score = 0
                if 3 in dice_count:
                    for d in dice_set:
                        x = d.value
                        self.three_kind_score += x
                        self.total += x
        if category == "four of a kind":
            if self.four_kind_score < 0:
                count = 0
                self.four_kind_score = 0
                if 4 in dice_count:
                    for d in dice_set:
                        x = d.value
                        self.four_kind_score += x
                        self.total += x

        else:
            print("Invalid slot")
        return count
class Die:
    value = 0
    def __init__(self):
        pass

    def roll(self):
       self.value = random.randint(1,6)
def print_scorecard(scorecard):
    x = [scorecard.ones_score,scorecard.twos_score,scorecard.threes_score,scorecard.fours_score,scorecard.fives_score,scorecard.sixes_score, scorecard.yahtzee_score, scorecard.full_house_score,scorecard.three_kind_score,scorecard.four_kind_score]
    print(x)
    return x
set0 = []
scorecard = Scorecard()
count = 0
def show_score(scorecard):
    print(f"Ones Score: {scorecard.ones_score}\nTwos Score: {scorecard.twos_score}\nThrees Score: {scorecard.threes_score}\nFours Score: {scorecard.fours_score}\nFives Score: {scorecard.fives_score}\nSixes Score: {scorecard.sixes_score}\nYahtzee: {scorecard.yahtzee_score}\nFull House: {scorecard.full_house_score}\nThree of a Kind: {scorecard.three_kind_score}\nFour of a Kind: {scorecard.four_kind_score}\nTotal: {scorecard.total}")
def count_values(dice_set, v):
    result = 0
    for d in dice_set:
        if d.value == v:
            result += 1
    return result
def count_dice(set0):
    set_count = []
    print(set0)
    set_count.append(count_values(set0,1))
    set_count.append(count_values(set0,2))
    set_count.append(count_values(set0,3))
    set_count.append(count_values(set0,4))
    set_count.append(count_values(set0,5))
    set_count.append(count_values(set0,6))
    print(set_count)
    return set_count


def print_set(set0):
    print(f"Dice 1: {set0[0].value}\n Dice 2: {set0[1].value}\n Dice 3: {set0[2].value}\n Dice 4: {set0[3].value}\n Dice 5: {set0[4].value}\n")
for i in range(0,5):
    dice = Die()
    dice.roll()
    set0.append(dice)
for i in range (0, 10):  
    reroll = "1 2 3 4 5"
    x = reroll.split()
    for i in x:  
        set0[int(i)-1].roll()

    print_set(set0)
    reroll = input("Which dice would you like to reroll")
    x = reroll.split()
    for i in x:  
        set0[int(i)-1].roll()
    print_set(set0)
    
    

    reroll = input("Which dice would you like to reroll")
    x = reroll.split()
    for i in x:  
        set0[int(i)-1].roll()
    print_set(set0)
    set_count = count_dice(set0)




    show_score(scorecard)
    scoring = input(f"Where would you like to score this?")
    f = -1
    while f < 0:
        f = scorecard.add_score(scoring, set0, set_count)
    show_score(scorecard)
x = print_scorecard(scorecard)
with open('output.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    if file.tell() == 0:
        writer.writerow(['ones','twos','threes','fours','fives','sixes','yahtzee','full house','three of a kind','four of a kind'])
    writer.writerow(x)    
