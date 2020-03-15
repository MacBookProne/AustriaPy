import food, fruits, candy

# Create various Food objects
a = fruits.Apple()
b = fruits.Banana()
c = food.Food("cheeseburger", 263)
p = fruits.Fruit("pear", 57)
s = candy.Snickers()
k = candy.KitKat()
ks = candy.Candy("Kinder Surprise", 113)

meal = [a,b,c,s,k,p,ks] # list of food objects

# loop through food objects and print them as strings 
print("My meal: ")
for dish in meal:
	print(str(dish))

# Test reverse adding 
print("Total calories",sum(meal))

# Test adding and comparing
print()
print("Is an", a.getName(), "and a", b.getName(), "together more calories than a", c.getName()+'?')
print("Answer:", a+b > c)
print()

# Test inheritance
print("Is an", a.getName(),"a fruit?")
print("Answer:",isinstance(a, fruits.Fruit))
print()
print("Is a", c.getName(),"a fruit?")
print("Answer:",isinstance(c, fruits.Fruit))
print()

# Test integer conversion
print("How many calories do 3", a.getName()+'s',"have?")
print("Answer:",int(a)*3)

#### DO NOT EDIT ABOVE THIS LINE ####


