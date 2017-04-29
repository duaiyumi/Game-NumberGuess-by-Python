import random

secret = random.randint(1,100)
guess = 0
tries = 0

print ("Guess a number from 0-99.You got a 6 chance.")
print ("Let's start!")

while guess != secret and tries < 6:
    guess = input("choice: ")
    if guess < secret:
        print ("Low!")
        tries = tries + 1
        
    elif guess > secret:
        print ("High!")
        tries = tries + 1
        
if guess == secret:
    print ("Yeah!You got it!")

else:
    print "Answer:", secret
