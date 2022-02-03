#rounds a number
#be careful of round, it rounds to the nearest even nimber
#eg 4.5 rounds to 4
#but 5.5 rounds to 6
#so do not use if accuracy is essential
#Author: Brid Kennedy

from numpy import number


numberToRound = float(input("Enter a float number: "))
roundedNumber = round (numberToRound)
print ('{} rounded is {}'.format(numberToRound,roundedNumber))