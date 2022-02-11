#a program to tell the user if a number is even or odd
# Author: Brid Kennedy

number = int(input("enter an integer:"))


if (number % 2) ==0:
    print ("{} is an even number".format(number))
else:
    print ("{} is an odd number".format(number))