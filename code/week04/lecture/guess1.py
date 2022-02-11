# promts the user to guess a number and keeps prompting
# Author: Brid Kennedy


numberToGuess = 30
guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("too low")
    else:
        print ("too high")

    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was ", numberToGuess)
