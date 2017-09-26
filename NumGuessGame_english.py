# coding=utf-8
    # Easy to use in Chinese version, using UTF-8 characters

import random
secret = random.randint(1,100)
guess = int(0)
tries = int(0)
    # Load the random number module and generate a 1-99 random integer for the answer. And the "guess number" (guess) and "tries" initialization.

print("AHOY! I'm the Dread Pirate Roberts, and I have a secret!")
print("It is a number from 1 to 99. I'll give you 6 tries.")
    # Opening remarks,"AHOY! I'm the Dread Pirate Roberts, and I have a secret!"
    # Opening remarks,""It is a number from 1 to 99. I'll give you 6 tries."

while int(guess) != secret and tries < 6:
    guess = input("What's yer guess?")
    # The starting condition of the game determines that when the number of guesses is not equal to the answer and the number of guesses is valid, the guessing begins.

    if int(guess) == 724:
        print(secret)
    # For the "BF" reserved for the back door, view random integers directly. The default value is 724.

    elif int(guess) < 0 or int(guess) > 99:
        print("Out of bounds!")
    # Check whether the user input value matches the range.

    elif int(guess) < secret and -1 < int(guess) < 100:
        print("Too low, ye scurvy dog!")
    # User input value is lower than random integer.

    elif int(guess) > secret and -1 < int(guess) < 100:
        print("Too high, landlubber !")
    # The user input value is higher than the random integer.

    tries = tries + 1
    # For each round, the number of times +1.

if int(guess) == secret:
    print("Avast! ye got it ! Found my secret, ye did!")
    # The user guessed yes, the output prompt.

elif tries == 6:
    print("No more guesses! Better luck next time, matey!")
    print("The secret number was:", secret)
    # The user has run out of chance and output the answer.
