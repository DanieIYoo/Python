#Guessing game
#import random 

import random 
top_of_range = input("""I generate a random number from 0. You need to give me the maximum.  
Give it a try, give me any number :  """)

if top_of_range.isdigit():
	top_of_range = int(top_of_range)
	
	if top_of_range <= 0:
		print("Please enter number above 0 ")
		quit()
else:
	print("It needs to be number!")
	quit()

random_number = random.randint(0, top_of_range)
guesses = 0
while True:
	guesses +=1
	if guesses == 10:
		print("Exceeded maximum 10 attempts! Bye")
		quit()
	user_guess = input("Okay let's guess the random number: ")
	
	if user_guess.isdigit():
		user_guess = int(user_guess)
	else:
		print("Need a number!")
		continue
	
	if user_guess == random_number:
		print("Correct!")
		print(guesses," guesses! Good Job")
		break
	
	elif user_guess > random_number:
		hint1 = ((user_guess) - (random_number))
		print("Hint: " + str(hint1))
		continue		
	else:
		print("Up! ")
		continue
	




