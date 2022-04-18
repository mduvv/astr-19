'''


'''

import numpy as np		# import numpy librabry


# This defines our main()
# function for our program
def main():

	i = 0 # integer
	n = 10 # another integer
	x = 19.0 # floating point number

	# we can use numpy to declare arrays quickly

	y = np.zeros(n, dtype=float) # declares ten 0.0's

	# we can use for loops to iterate with a variable

	for i in range(n): # loop from i=0 to i=n-1
		y[i] = 2.0 * float(i) + 1 # sets y = 2*i+1 as floats


	#we can also simply iterate through a variable	
	for y_element in y:
		print(y_element)



# When we run the program
# this executes first
if __name__ == '__main__':
	main()


