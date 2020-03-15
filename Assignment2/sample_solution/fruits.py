from food import Food

class Fruit(Food):
	"""Fruit inherits from Food and overwrites __str__"""

	def __init__(self, name, calories):
		"""Fruit constructor calls Food constructor"""
		Food.__init__(self, name, calories)

	def __str__(self):
		"""Overload str() function of Food"""
		return self.name + " is a fruit and has " + str(self.calories) + " calories."

class Apple(Fruit):
	"""
	Apple inherits from Fruit
	name = "apple"
	calories = 52
	"""

	def __init__(self):
		"""Apple constructor calls Fruit constructor"""
		Fruit.__init__(self, "apple", 52)

class Banana(Fruit):
	"""
	Banana inherits from Fruit
	name = "banana"
	calories = 94
	"""

	def __init__(self):
		"""Banana constructor calls Fruit constructor"""
		Fruit.__init__(self, "banana", 94)
