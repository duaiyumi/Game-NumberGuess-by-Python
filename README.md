# Game-NumberGuess-by-Python_My first program.
Chinese：
  我从《与孩子一起学编程（作者桑德）》看到一个随机数的游戏，因吹斯汀。这是python2的，我感兴趣，用python3改写了，加入了老马风格的内容，有以下特性：
	1.加入了条件判定，不在范围内的数字提示超出范围。
	2.加入了直接看答案的代码，单从这游戏来看没什么意义，但它意味着部分用户有着很大的权限。
	3.（强迫症凑数用）
#欢迎各位提供意见！
	
源码如下：

import random

secret = random.ranint(1,100)
guess = 0
tries = 0

print "AHOY! I'm the Dread Pirate Roberts, and I have a secret!"
print "It is a number from 1 to 99. I'll give you 6 tries."

while guess != secret and tries <6:
	guess = input("What's yer guess?")
	if guess < secret:
		print "Too low, ye scurvy dog!"
	elif guess > secret:
		print "Too high, landlubber !"
	tries = tries +1

if guess == secret:
	print "Avast! ye got it ! Found my secret, ye did!"
else:
	print "No more guesses! Better luck next time, matey!"
	print "The secret number was", secret
  
English:
  I saw a random number game from the "Hello World! Computer Programming for Kids and Other Beginners"Author isWarren Sande, Carter Sande , that‘s interesting. This is python2, and I'm interested in using python3 to rewrite the content added to the nag style, with the following features:
  1. joined the condition judgment, not in the scope of the digital prompt out of range.
  2. adding code that looks directly at the answer doesn't make sense, but it means that some users have a lot of privileges.
  3. (dine with OCD)
  # welcome advice!
  Source code is as follows:
  
  import random

secret = random.ranint(1,100)
guess = 0
tries = 0

print "AHOY! I'm the Dread Pirate Roberts, and I have a secret!"
print "It is a number from 1 to 99. I'll give you 6 tries."

while guess != secret and tries <6:
	guess = input("What's yer guess?")
	if guess < secret:
		print "Too low, ye scurvy dog!"
	elif guess > secret:
		print "Too high, landlubber !"
	tries = tries +1

if guess == secret:
	print "Avast! ye got it ! Found my secret, ye did!"
else:
	print "No more guesses! Better luck next time, matey!"
	print "The secret number was", secret
