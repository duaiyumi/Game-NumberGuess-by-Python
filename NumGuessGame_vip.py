#coding=utf-8
import random

secret = random.randint(0,99)
guess = 0
tries = 0

print ("Aha！我是可怕的海盗罗伯茨，我有一个秘密！")
print ("猜一个0到99的数字。我给你6次机会。")

while guess != secret and tries < 6:
    guess = input("选一个吧: ")
    if int(guess) < secret:
        print ("太低喽。")        
    elif int(guess) > secret:
        print ("太高了！")
    tries = tries + 1
        
if guess == secret:
    print ("Yeah！你猜对了！")

else:
    print "Answer:", secret
