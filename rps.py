import random

# get input and save it in variable player
player = input("Rock, paper, or scissors?")

# get random number between 1 - 3
computer = random.randint(1,3)

# print statement
print("hello world")

# if-elif-if statement
if player == "dog":
	print("it's a dog!")
elif player == "cat":
	print("it's a cat!")
elif player == "mouse":
	print("it's a mouse!")
else:
	print("it's not a cat, a dog, or a mouse!")
	