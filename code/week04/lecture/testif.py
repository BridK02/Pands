# Program to show the format of an if statement
#Author: Brid Kennedy

from sqlalchemy import false, true


if false:
    #statements
    print("condition is true")
b = 2
if b == 3:
    print("yes the world is sane")
else:
    print("b is not equal to 2")
a = 2
if a != 2:
    print("I hope this is not displayed!!!!")
else:
    print("2 is not equal to 2 is false")

    aNumber = 5
    if (aNumber % 2) == 0: # brackets for clarity
        print(aNumber, "is even") # another way of printing variables
    elif (aNumber % 3) == 0: # if the number is even this will not be checked
        print(aNumber, "is divisable by 3")
    else:
        print(aNumber, "is not even or divisable by 3")

    print ("this will always be outputted")