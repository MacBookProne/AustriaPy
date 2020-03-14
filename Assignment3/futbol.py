# Team members:             #
# Justin O'Dea              #
# Lluc Cardoner             #
#############################
# Numpy module              #
#############################

import numpy as np

# Christiano Ronaldo goals with R.M. in each year
league = np.array([26, 40, 46, 34, 31, 48, 35, 25])
cup = np.array([0, 7, 3, 7, 3, 1, 0, 1])
europe = np.array([7, 6, 10, 12, 17, 10, 16, 10])
competitions = [league, cup, europe]

# Print example:
# print("My name is {} and I am {} years old.".format(name, years))

# Numpy functions:
# nonzeros(), mean(), sum(), max(), min()

# TODO 1.1 Calculate the max amount of goals that Ronaldo has made in one year. Print the results


# TODO 1.2 Calculate the max amount of goals that he has made in League, Cup, Europe. Print the results


# TODO 1.3 Calculate the min amount of goals that Ronaldo has made in one year. Print the results


# TODO 1.4 Calculate the min amount of goals that he has made in League, Cup, Europe. Print the results


# TODO 2 Count in how many years Ronaldo has made 0 goals in each competition. Print the results


# TODO 3 Calculate the total number of goals for each competition and in his whole career. Print the results
sum = [0, 0, 0]
for i, competition in enumerate(competitions):
    pass  # calculate for each competition
total = 0  # change
print("Total goals - League: {}, Cup: {}, Europe: {}, All competitions: {}".format(sum[0], sum[1], sum[2], total))

# TODO 4 Calculate the average goals for each competition. Print the results
avg = [0, 0, 0]
for i, competition in enumerate(competitions):
    pass  # calculate for each competition
print("Average goals - League: {}, Cup: {}, Europe: {}".format(avg[0], avg[1], avg[2]))

# TODO 5 Use the numpy package to create a matrix with the goals of the 3 competitions in each row. Print the results

# TODO 6 Get a new matrix made of the number of goals of the second and third year of League and Cup and print it neatly. 

