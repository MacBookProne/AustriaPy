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
					'actor_2_name', 'actor_3_name', 'imdb_score', 'movie_facebook_likes']		#list of columns that should be kept

	old_data = pd.read_csv("movie_metadata.csv")												#reads the old csv data
	df = old_data.loc[:, keep_columns]															#filters the old data and creates a new dataframe with only the columns in keep_columns

	for i in range(0,df.shape[0]):																#a for loop that strips white space from all values in the movie_title column, not necessary
		df.iloc[i,0] = df.iloc[i,0].strip()										

	df.to_csv("movies.csv", sep=",", encoding = "utf-8")										#write to the new csv file

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
	choices = ["budget", "gross", "imdb", "likes"]												
	columns = ['budget', 'gross', 'imdb_score', 'movie_facebook_likes']							#used to translate the index from the user choice into the column name

	choice = input("Choose a metric (budget/gross/imdb/likes): ")

	if(choice.lower() in choices):																#checks if choice is correct
		index = choices.index(choice)															#translates the choice
		sorted_values = df.sort_values([columns[index]], ascending=False)						#sorts the values based on the column from the user choice
		printing = sorted_values[:10].movie_title.values.tolist()
		print("\nTop 10 movies with highest " + choice +":\n")
		#print(*printing, sep='\n')
	else:
		print("Invalid input...")

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
	movie_name = input("Enter a movie name: ")
	movie = df[df.movie_title.str.lower() == movie_name.lower()]								#searches the dataframe for the specified movie

	if movie.shape[0] == 0:																		#checks if there were results, if not then exit the function
		print("No results found for '" + movie_name + "'")
		return

	#assign all the variable that will be printed later with the relevant values, and convert them to strings where needed
	title = movie.movie_title.tolist()[0]
	director = movie.director_name.tolist()[0]
	country = movie.country.tolist()[0]
	year = str(int(movie.title_year.tolist()[0]))
	score = str(movie.imdb_score.tolist()[0])
	likes = str(int(movie.movie_facebook_likes.tolist()[0]))
	budget = str(int(movie.budget.tolist()[0]))
	gross = str(int(movie.gross.tolist()[0]))

	#print the summary in a neat format
	print("\nThe movie '" + title + "' directed by " + director + ", was released in " 
			+ country + " in the year " + year + ". The budget of the movie was " 
			+ budget + "$ and it brought in " + gross + "$. The movie received an imdb score of " 
			+ score + " and " + likes + " of facebook likes.")	

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

	country_list = df.country.unique()															#find all countries in the dataframe
	minYear = int(df.title_year.min())
	maxYear = int(df.title_year.max())

	#while() loop that runs until user inputs a correct country
	while(True):

		country = input("Enter a country (type 'list' for a list of available countries): ")	#ask the user for a country and store it in country variable

		if(country.lower() in ([str(x).lower() for x in country_list])):
			break
		elif country == "list":
			print(country_list)
		else:
			print("Invalid input...")

	#while() loop that runs until user inputs a correct year
	while(True):

		year = int(input("Enter a year (" + str(minYear) + "-" + str(maxYear) + "): "))			#ask the user for a year and store it in year variable

		if year in range(minYear, maxYear):
			break
		else:
			print("Invalid input...")

	#filter dataframe based on country and year variables
	data_filter = (df.country.str.lower() == country.lower()) & (df.title_year == year)			
	data = df[data_filter]

	#check if resulting dataframe after filter is empty. If yes, print "no results found" and exit the function
	if data.shape[0] == 0:
		print("No results found for '" + country + "', in the year " + str(year) + "...")
		return
	else:
		#assign all the values and convert to strings
		moviesFilmed = str(data.shape[0])
		maxBudgetMovie = str(data[data.budget == data.budget.max()].iloc[0 ,1])
		minBudgetMovie = str(data[data.budget == data.budget.min()].iloc[0 ,1])
		maxGrossMovie = str(data[data.gross == data.gross.max()].iloc[0 ,1])
		maxGrossIMDB = str(data[data.gross == data.gross.max()].iloc[0 ,15])
		maxGrossLikes = str(data[data.gross == data.gross.max()].iloc[0 ,16])

		#print the neat summary with all the necessary values from above
		print("\n" + moviesFilmed + " movies were filmed in " + country + " during " + str(year) + "."
				+  " The movie with the highest budget (" + str(data.budget.max()) + "$), was '" + maxBudgetMovie + "'"
				+ ", and the movie with lowest budget (" + str(data.budget.min()) + "$), was '" + minBudgetMovie + "'. "
				+ "The movie with the highest gross (" + str(data.gross.max()) + "$), was '" + maxGrossMovie
				+ "' (with an IMDB rating of " + maxGrossIMDB + " and " + maxGrossLikes + " facebook likes)" + ".")

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

	top10 = df['director_name'].value_counts()[:10]												#finds the top 10 directors with most movies directed
	directors = top10.index.tolist()															#list containing director names
	movies = top10.values.tolist()																#list containing number of movies 

	#print the table header with all information in a neat format
	print("\n")
	print('%5s | %18s | %14s | %12s | %12s | %12s ' % ("#", "Director name", "Movies directed", "Avg Gross", "Avg IMDB", "Avg likes"))
	print('------------------------------------------------------------------------------------------')
	
	#a for loop that goes through all the directors and prints out the information in rows containing all the data related to that director
	for i in range(0,10):
		avgGross = int(df[df.director_name == directors[i]].gross.mean())
		avgIMDB = int(df[df.director_name == directors[i]].imdb_score.mean())
		avgLikes = int(df[df.director_name == directors[i]].movie_facebook_likes.mean())
		print('%5s | %18s | %15s | %12s | %12s | %12s ' % (str(i+1), directors[i], movies[i], avgGross, avgIMDB, avgLikes))

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