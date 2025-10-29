import random

class Die:
    def __init__(self, sides=6):
        self.sides = int(sides)  # sets the sides attribute for this Die object
    
    def roll(self):
        return random.randint(1, self.sides)  # uses the sides value of this Die object

class DiceGame:
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()
    
    def play_round(self):
        v1 = self.die1.roll()
        v2 = self.die2.roll()
        total = v1 + v2
        result = self.evaluate_roll(total)
        return v1, v2, total, result
    
    def evaluate_roll(self, total):
        if total in (7, 11):
            return "Win"
        if total in (2, 3, 12):
            return "Lose"
        return "Roll Again"