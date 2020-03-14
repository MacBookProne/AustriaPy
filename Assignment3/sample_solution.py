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

# TODO Calculate the max amount of goals that Ronaldo has made in one year
max_league = league.max()
max_cup = cup.max()
max_europe = europe.max()
print("Max goals in League: {}".format(max_league))
print("Max goals in Cup: {}".format(max_cup))
print("Max goals in Europe: {}".format(max_europe))

# TODO Calculate the max amount of goals that he has made in League, Cup, Europe
max_total = np.array([max_league, max_cup, max_europe]).max()
print("Max goals in League, Cup and Europe: {}".format(max_total))

# TODO Calculate the min amount of goals that Ronaldo has made in one year
min_league = league.min()
min_cup = cup.min()
min_europe = europe.min()
print("Min goals in League: {}".format(min_league))
print("Min goals in Cup: {}".format(min_cup))
print("Min goals in Europe: {}".format(min_europe))

# TODO Calculate the min amount of goals that he has made in League, Cup, Europe
min_total = np.array([min_league, min_cup, min_europe]).min()
print("Min goals in League, Cup and Europe: {}".format(min_total))

# TODO Count in how many years Ronaldo has made 0 goals in each competition
league_zeros = len(league) - len(league.nonzero()[0])
cup_zeros = len(cup) - len(cup.nonzero()[0])
europe_zeros = len(europe) - len(europe.nonzero()[0])
print("Number of Years with 0 goals at League is {} out of {}".format(league_zeros, len(league)))
print("Number of Years with 0 goals at Cup is {} out of {}".format(cup_zeros, len(cup)))
print("Number of Years with 0 goals at Europe is {} out of {}".format(europe_zeros, len(europe)))

# TODO Calculate the total number of goals for each competition and in his whole career
sum = [0, 0, 0]
for i, competition in enumerate(competitions):
    sum[i] = competition.sum()
total = np.array(sum).sum()
print("Total goals - League: {}, Cup: {}, Europe: {}, All competitions: {}".format(sum[0], sum[1], sum[2], total))

# TODO Calculate the average of goals for each competition
avg = [0, 0, 0]
for i, competition in enumerate(competitions):
    avg[i] = competition.mean()
print("Average goals - League: {}, Cup: {}, Europe: {}".format(avg[0], avg[1], avg[2]))

# TODO Use the numpy package to create a matrix with the goals of the 3 competitions in each row
mat = np.array([league, cup, europe])
print(mat)

# TODO Build a new matrix made from the number of goals of the second and third year of League and Cup and print it neatly sample_solution.py
new_mat = mat[:2, 1:3]
print("League: second and third year: {}".format(new_mat[0]))
print("Cup: second and third year: {}".format(new_mat[1]))


