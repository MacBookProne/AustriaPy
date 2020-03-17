# --------------------------------
# Python!
# Authors: Justin and Gabriel
# --------------------------------
# DataType Assignment
# --------------------------------

full_name = input("Enter your full name: ")         #data_type: string

height_inch = input("Enter your height (inch): ")   #data type: string
height_inch = float(height_inch)                    #conversion: string -> float
weight_lb = input("Enter your weight (lb): ")       #data type: string
weight_lb = float(weight_lb)                        #conversion: string -> float

color_eyes = input("Enter your eye color: ")        #data_type: string
color_hair = input("Enter your hair color: ")       #data_type: string

#task 1:    your modified program should use float variables to store the height and weight
#see above

#task 2:    calculate how many characters your full name has:
len_full_name = len(full_name)  #data type: int


#task 3:    intruduce two new variables height_cm of the type integer and weight_kg of the type float
#           convert your height/weight from inch/lb into the metric system (meters/kilograms) and save the result into the corresponding variables
height_cm = height_inch*2.54    #data type: float
height_cm = int(height_cm)      #conversion: float -> int
weight_kg = weight_lb*0.453592  #data type: float

#task 4:    calculate the bodymassindex and introduce a new float variable to save it
#           hint: Calculation: [weight (lb) / height (in) / height (in)] x 703
bmi = (weight_lb/height_inch/height_inch)*703    #data type: float

#task 5:    print a summary containing all information above
print("Summary:")
print("Full name : ", full_name, " (", len_full_name, " characters)")
print("Height: ", height_inch, " inches (", height_cm, " centimeters)")
print("Weight: ", weight_lb, " pounds (", weight_kg, " kilograms)")
print("Resulting bodymassindex: ", bmi)
print("Eye color: " , color_eyes)
print("Hair color: ", color_hair)


#task 6:    add comments explaining the variable/data type conversions your program is doing
#see above