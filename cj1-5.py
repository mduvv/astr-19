'''
Write a Python program that writes out a table of the function sin(x) vs. x, where
x is tabulated between 0 and 2pi with a thousand entries. Follow the basic Python program
structure, including a main program function.

'''

import numpy as np

def main():
    print("sin(x) vs x")
    print("-"*50)
    x = 2
    z = np.linspace(0.0, 2.0*np.pi, num=10, dtype=float) # array from 0.0 to 2.0 with a 1000 entries
    for item in z:
        print(f"{np.sin(item):>} {item:>} ") # left align


# When we run the program
# this executes first
if __name__=="__main__":
	main()