'''
Write a Python program that defines a function f(x) that
returns x**3 + 8. In the main function of the program, 
call f(x) with x = 9 and print the result.
Use an if statement that executes if the result is larger than 27
and prints “YAY!”.

'''

import numpy as np		# import numpy librabry

# function f(x) that returns x**3 + 8
def f(x):
	return x**3 + 8	


# This defines our main()
# function for our program
def main():

	x = 9
	
	print(f(x))

	if f(x) > 27:
		print("YAY!")



# When we run the program
# this executes first
if __name__ == '__main__':
	main()


