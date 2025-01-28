
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

    def add_score(self, category, dice_set, dice_count, should_update):
        count = -1
        if category == "ones":
            if self.ones_score < 0:
                count = 0
                for d in dice_set:
                    if d.value == 1:
                        print("found a one")
                        count += 1
                if should_update == True:
                    self.ones_score = count
                    self.total += count
            else:
              count = -1
              print("invalid - you used ones already")
        if category == "twos":
            if self.twos_score < 0:
                count = 0
                for d in dice_set:
                    if d.value == 2:
                        print("found a two")
                        count += 2
                if should_update == True:
                    self.twos_score = count
                    self.total += count
            else:
                count = -1
                print("invalid - you used twos already") 
        if category == "threes":
            if self.threes_score < 0:
                count = 0
                for d in dice_set:
                    if d.value == 3:
                        print("found a three")
                        count += 3
                if should_update == True:
                    self.threes_score = count
                    self.total += count
            else:
                count = -1
                print("invalid - you used threes already")
        if category == "fours":
            if self.fours_score < 0:
                count = 0
                for d in dice_set:
                    if d.value == 4:
                        print("found a four")
                        count += 4
                if should_update == True:
                    self.fours_score = count
                    self.total += count
            else:
                count = -1
                print("invalid - you used fours already")
        if category == "fives":
            if self.fives_score < 0:
                count = 0
                for d in dice_set:
                    if d.value == 5:
                        count += 5
                if should_update == True:
                    self.fives_score = count
                    self.total += count
            else:
                count = -1
                print("invalid - you used fives already")
        if category == "sixes":
            if self.sixes_score < 0:
                count = 0
                for d in dice_set:
                    if d.value == 6:
                        print("found a six")
                        count += 6
                if should_update == True:
                    self.sixes_score = count
                    self.total += count
            else:
                count = -1
                print("invalid - you used sixes already")
        if category == "yahtzee":
            if self.yahtzee_score < 0:
                count = 0
                if 5 in dice_count:
                    # we have a yahtzee
                    count = 50                    
                if should_update == True:
                    self.yahtzee_score = count
                    self.total += count
            else:
                count = -1
        if category == "full house":
            if self.full_house_score < 0:
                count = 0
                if 2 in dice_count:
                    if 3 in dice_count:
                        count = 25              
                if should_update == True:
                    self.full_house_score = count
                    self.total += count
            else:
                count = -1
        if category == "three of a kind":
            if self.three_kind_score < 0:
                count = 0
                if 3 in dice_count:
                    for d in dice_set:
                        count += d.value              
                if should_update == True:
                    self.three_kind_score = count
                    self.total += count
            else:
                count = -1
        if category == "four of a kind":
            if self.four_kind_score < 0:
                count = 0
                if 4 in dice_count:
                    for d in dice_set:
                        count += d.value         
                if should_update == True:
                    self.four_kind_score = count
                    self.total += count
            else:
                count = -1
        return count
    
    def print_scorecard(self):
        x = [self.ones_score,self.twos_score,self.threes_score,self.fours_score,self.fives_score,self.sixes_score, self.yahtzee_score, self.full_house_score,self.three_kind_score,self.four_kind_score]
        print(x)
        return x
    def show_score(self):
        print(f"Ones Score: {self.ones_score}\nTwos Score: {self.twos_score}\nThrees Score: {self.threes_score}\nFours Score: {self.fours_score}\nFives Score: {self.fives_score}\nSixes Score: {self.sixes_score}\nYahtzee: {self.yahtzee_score}\nFull House: {self.full_house_score}\nThree of a Kind: {self.three_kind_score}\nFour of a Kind: {self.four_kind_score}\nTotal: {self .total}")
