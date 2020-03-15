from food import Food

class Candy(Food):
	"""Candy inherits from Food and overwrites __str__"""

	def __init__(self, name, calories):
		"""Candy constructor calls Food constructor"""
		Food.__init__(self, name, calories)

	def __str__(self):
		"""Overload str() function of Food"""
		return self.name + " is candy and has " + str(self.calories) + " calories."

class Snickers(Candy):
	"""
	Snickers inherits from Candy
	name = "Snickers"
	calories = 488
	"""
	
	def __init__(self):
		"""Snickers constructor calls Candy constructor"""
		Candy.__init__(self, "Snickers", 488)

class KitKat(Candy):
	"""
	KitKat inherits from Candy
	name = "KitKat"
	calories = 518
	"""

	def __init__(self):
		"""KitKat constructor calls Candy constructor"""
		Candy.__init__(self, "KitKat", 518)



