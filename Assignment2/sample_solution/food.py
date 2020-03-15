class Food:
    """
    A food object has a name and calories.
    Food objects are comparable and add-able by calories.
    """
    
    def __init__(self, name, calories):
        """Food constructor"""
        self.name = name
        self.calories = calories
        
    def getName(self):
        return self.name
        
    def getCalories(self):
        return self.calories
        
    def __str__(self):
        """Turn a food object into a string"""
        return self.name + " has " + str(self.calories) + " calories."
    
    def __int__(self):
        """Turn food object into an int (calories)"""
        return self.calories
    
    def __radd__(self, other):
        """Reverse adding required to add food objects with each other, e.g. sum"""
        return self.calories + other
        
    def __add__(self, other):
        """add a food object with something else"""
        return self.calories + other
    
    def __lt__(self, other):
        """Less than comparator"""
        return self.calories < other

    def __le__(self, other):
        """Less than or comparator"""
        return self.calories <= other

    def __eq__(self, other):
        """Equality comparator"""
        return self.calories == other

    def __ne__(self, other):
        """Non-equality comparator"""
        return self.calories != other

    def __gt__(self, other):
        """Greater than comparator"""
        return self.calories > other

    def __ge__(self, other):
        """Greater than or equal comparator"""
        return self.calories >= other
        
        
