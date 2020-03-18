import pandas as pd 					#import pythons pandas library as alias pd
import numpy as np 						#importing pythons numpy library as alias np
import matplotlib.pyplot as plt 		#importing pythons matlab library as alias plt

'''
The function printMenu() is used to print out the menu and display all the options to the user
'''
def printMenu():
	print("\n MENU:")
	print("--------------------------------------")
	print("1. Top 10 all time movies")
	print("2. Show movie information")
	print("3. Analyze movies by country and year")
	print("4. Show top 10 directors statistics")
	print("5. Exit")
	print("--------------------------------------")
	print("\n")

'''
The function new_csv() is used to clean up the given movie_metadata.csv file and create a new one called movies.csv

The function reads from the provided movie_metadata.csv file and creates a new file that contains only columns used in our program

Hint: use the provided list of columns to create the new movies.csv file
'''
def new_csv():
	keep_columns = ['movie_title', 'duration', 'color', 'genres', 
					'plot_keywords', 'country', 'title_year', 'language', 
					'budget', 'gross', 'director_name', 'actor_1_name', 
					'actor_2_name', 'actor_3_name', 'imdb_score', 'movie_facebook_likes']

	#WRITE YOUR CODE FOR TASK 1 HERE
	
	return

'''
The function import_csv() is used to read the movies.csv file. It returns a panda dataframe that contains all the data from the csv file. 
'''
def import_csv():
	df = pd.read_csv("movies.csv")
	return df

'''
The function top10Movies() takes a panda dataframe as input variable and asks the user for input on which metric to sort the top 10

Based on the user input, it prints out a list of 10 movies with the highest selected metric 
'''
def top10Movies(df):

	#WRITE YOUR CODE FOR TASK 2 HERE

	return

'''
The function showMovieInfo() takes a panda dataframe as input variable and asks the user for input of a movie title

Based on the input, the function prints out a summary of the movie with the following information:

	- movie title
	- name of director
	- country in which the movie was released
	- release year
	- budget and gross of the movie
	- imdb score
	- amount of facebook likes
'''
def showMovieInfo(df):

	#WRITE YOUR CODE FOR TASK 3 HERE

	return

'''
The function analyseMovies() takes a panda dataframe as input variable and asks the user for input of a Country and Year

Based on the input, the function returns a summary of the movies released in the specified year and country.

The summary contains the following information:

	- Number of movies filmed in that country and year
	- Movie with highest budget
	- Movie with lowest budget
	- Movie with highest gross and its IMDB rating and amount of facebook likes
'''
def analyseMovies(df):

	#WRITE YOUR CODE FOR TASK 4 HERE

	return

'''
The function topDirectors() takes a panda dataframe as input variable and prints out information about the 10 directors that directed the most movies.

The function prints the information in a neat tabel within the console, sorted from highest to lowest. The information contained in the table is:

	- Director name
	- Number of movies directed
	- Average gross of his movies
	- Average IMDB score of his movies
	- Average amount of facebook likes of his movies
'''
def topDirectors(df):

	#WRITE YOUR CODE FOR TASK 5 HERE

	return

def main():

	#calls the function that creates a new csv file called movies.csv 
	new_csv()

	#import movies.csv and assign the data to a variable called "data"
	data = import_csv()

	#while loop that runs as long as user doesn't exit the program by selecting 5th option
	while(True):

		#prints the menu
		printMenu()

		#asks for user input on what function to call
		user_input = input("Choose an option (1-5): ")

		#depending on the user input call the respective function
		if user_input == "1":
			top10Movies(data)
		elif user_input == "2":
			showMovieInfo(data)	
		elif user_input == "3":
			analyseMovies(data)
		elif user_input == "4":
			topDirectors(data)
		elif user_input == "5":
			#exit the program
			raise SystemExit
		else:
			print("Incorrect input... must be a number between 1 and 5")
			#warns the user of incorrect input and continues with the while() loop
			continue

#Used to call the main function at startup
if __name__ == "__main__":
    main()