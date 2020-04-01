class State:

    def __init__(self, german_name, english_name, population, capital):
        self.german_name = german_name
        self.english_name = english_name
        self.population = population
        self.capital = capital

    def get_population(self):
        return self.population

    def get_german_name(self):
        return self.german_name