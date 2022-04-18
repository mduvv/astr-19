'''
Write a Python that prints the sum of two floating point numbers,
the difference between two integers, and the product
of a floating point number and an integer.
In each case, have the program print out the data type of the
resulting answer.

'''

import numpy as np		# import numpy librabry

# function to print out sum and data type
def sum(x, y):
	sum = x + y
	print(sum, type(sum))


# function to print out difference and data type
def difference(x, y):
	diff = x - y
	print(diff, type(diff))

# function to print out product and data type
def product(x, y):
	product = x * y
	print(product, type(product))

# This defines our main()
# function for our program
def main():
	fp1 = 5.0			# first floating point
	fp2 = 7.0			# second floating point
	int1 = 4			# first integer number
	int2 = 9			# second integer number

	sum(fp1, fp2)
	difference(int2, int1)
	product(fp1, int1)

# When we run the program
# this executes first
if __name__ == '__main__':
	main()

