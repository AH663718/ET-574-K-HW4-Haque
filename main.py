# Azmal Haque - 24629956

import random


class Die:
	def __init__(self, sides=6):
		if sides < 1:
			raise ValueError("Die must have at least one side")
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


def main():
	"""Simple console menu:

	1. Play a round
	2. Exit

	When playing, displays the two dice, the total, and the result.
	"""
	game = DiceGame()
	while True:
		print("\n1. Play a round")
		print("2. Exit")
		choice = input("Enter choice [1-2]: ").strip()
		if choice == "1":
			v1, v2, total, result = game.play_round()
			print(f"Die 1: {v1}  Die 2: {v2}  Total: {total}  Result: {result}")
		elif choice == "2":
			print("Goodbye!")
			break
		else:
			print("Invalid choice, please enter 1 or 2.")


if __name__ == "__main__":
	main()