import random

secret = random.randint(1, 100)
guess = int(0)
tries = int(0)

print("Guess a number from 0-99.You got a 6 chance.")
print("Let's start!")

while guess != secret and tries < 6:
    guess = input("choice: ")
    if int(guess) < secret:
        print("Low!")
    elif int(guess) > secret:
        print("High!")
    tries = tries + 1

if guess == secret:
    print("Yeah!You got it!")

else:
    print("Answer:", secret);
