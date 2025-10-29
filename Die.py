import random


class Die:
	"""A simple die with a configurable number of sides.

	Methods
	-------
	roll()
		Return a random integer between 1 and number of sides (inclusive).
	"""

	def __init__(self, sides=6):
		if sides < 1:
			raise ValueError("Die must have at least one side")
		self.sides = int(sides)

	def roll(self):
		"""Return a random integer between 1 and self.sides (inclusive)."""
		return random.randint(1, self.sides)