from Die import Die


class DiceGame:
	"""A simple dice game using two dice.

	Behavior/assumptions:
	- Two standard dice are created with 6 sides each by default.
	- play_round() returns a tuple: (die1_value, die2_value, total, result)
	- evaluate_roll(total) follows common craps-like rules:
		* total == 7 or 11 -> 'win'
		* total in (2, 3, 12) -> 'loss'
		* otherwise -> 'no decision' (neither immediate win nor loss)
	"""

	def __init__(self):
		self.die1 = Die()
		self.die2 = Die()

	def play_round(self):
		"""Roll both dice and return (value1, value2, total, result).

		result is the string returned by evaluate_roll(total).
		"""
		v1 = self.die1.roll()
		v2 = self.die2.roll()
		total = v1 + v2
		result = self.evaluate_roll(total)
		return v1, v2, total, result

	def evaluate_roll(self, total):
		"""Evaluate the total and return the outcome string.

		Mapping (per provided rules):
		- 7 or 11       -> 'Win'
		- 2, 3, or 12  -> 'Lose'
		- 4..6 or 8..10 -> 'Roll Again'
		"""
		if total in (7, 11):
			return "Win"
		if total in (2, 3, 12):
			return "Lose"
		# 4-6 and 8-10 fall here
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