'''
Write a Python program that declares a class describing your favorite animal.
Have the data members of the class represent the following physical parameters of
the animal: length of the arms (float), length of the legs (float), number of eyes (int), does it have a tail? (bool), is it furry? (bool).
Write an initialization function that sets the values of the data members when an instance of the class is created.
Write a member function of the class to print out and describe the data members representing the physical characteristics of the animal.
'''


import sys

# define Dog class
class Dog:

    # print function for charactersistics
    def print(self):
        print("Here are the physical characteristics of a dog!")
        print(f"Length of arms = {self.arm_length}")
        print(f"Length of legs = {self.leg_length}")
        print(f"Number of eyes = {self.num_eyes}")
        print(f"Does it have a tail? = {self.tail_bool}")
        print(f"Is it furry? = {self.furry_bool}")

    # initialize function
    def __init__(self, armlen = 0., leglen = 4., eyenum = 2, tail = True, furry = True):
        self.arm_length = armlen
        self.leg_length = leglen
        self.num_eyes = eyenum
        self.tail_bool = tail
        self.furry_bool = furry


# main function
def main():

    # initialize our dog
    my_dog = Dog()

    # print info about our dog
    my_dog.print()

# When we run the program
# this executes first
if __name__=="__main__":
	main()