#Quiz Game
print("Welcome to the world of numbers!")

playing = input("Would you like to play the game?  ")

if playing.lower() != "yes":
	print("Bye for now, I will miss you")
	quit()

print("Okay! Let's play!")
score = 0

answer = input("Q1.What does the CPU stand for? ")
if answer.lower() == "central processing unit":
	print('Correct!')
	score +=1
else:
	print("Wrong!")
	

answer= input("Q2.What does GPU stand for?  ")
if answer.lower() == "graphics processing unit":
	print('Correct!')
	score +=1
else:
	print("Wrong!")
	

answer = input("Q3.What does RAM stand for? ")
if answer.lower() == "random access memory":
	print('Correct!')
	score +=1
else:
	print("Wrong!")
	

answer = input("Q4 What does PS stand for? ")
if answer.lower() == "power supply":
	print('Correct!')
	score +=1
else:
	print("Wrong!")
	

print("You got " + str(score) + " questions correct")
print(str((score/4)*100) + "%")
	


