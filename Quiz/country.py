class Country:

	def __init__(self, german_name, english_name, population, capital):
		self.german_name = german_name
    	self.english_name = english_name
    	self.population = population
    	self.capital = capital

	def__repr_(self):
    	return repr((self.german_name, self.english_name, self.population, self.capital))
    def weighted_grade(self):
    	return "State, Population".index(self.population)

  ##https://wiki.python.org/moin/HowTo/Sorting

  ##was trying to understand how to implemt tuples I beileved this would be a good way to do this.
