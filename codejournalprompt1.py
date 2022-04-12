# Write a Python program to print out your full name, 
# your preferred pronouns (optional), and two sentences
# about your favorite movie and your favorite food


# This function prints out full name
def PrintFullName():
	print("Mohan Duvvuri")

# This function prints out preffered pronouns
def PrintPrefferedPronouns():
	print("He/Him")

# This function prints out two sentences about favorite food and movie
def PrintTwoSentencesAbtMovieAndFood():
	print("My favorite movie is Dead Poets Society by Peter Weir. My favorite food is a tie between chicken sandwhices and sushi.")
	
# This defines our main()
# function for our program
def main():
	PrintFullName()
	PrintPrefferedPronouns()
	PrintTwoSentencesAbtMovieAndFood()


# When we run the program
# this executes first
if __name__ == '__main__':
	main()