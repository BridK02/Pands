#program that reads in a students percentage and prints out the corresponding grade
# Author: Brid Kennedy

percentage = float(input("Enter the percentage:"))
#print (percentage)

if percentage < 0 or percentage> 100:
    # this should throw an error
    print ("Please enter a number between 0 and 100")
elif percentage < 40: # we already know its greater than 0
    print ("Fail")
elif percentage < 50: # between 40 and 49
    print ("Pass")
elif percentage < 60: # between 50 and 59
    print ("Merit1")
elif percentage < 70: 
    print ("Merit2")
else: print ("Distinction")