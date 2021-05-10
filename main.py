import time
from os import system
from encryption import encrypt,decrypt
system('clear')

print ("""Welcome to the ultimate Marvel quiz!
This is the hardest Marvel quiz you'll ever take."""
)
username = input ("What's your name: ")

instructionsquestion = input ("Would you like to see the instructions?,y/n: ")
if instructionsquestion == "y":
	print ("INSTRUCTIONS: You will be given a multiple choice question and in the input field you have to enter the letter that is in front of the correct answer")
	time.sleep(1)
	input("When you've read through the instructions, click the enter key...")
else:
	print ("In that case, let's go!!!")
time.sleep(2)
print ("Ready")
time.sleep(1)
print ("Steady")
time.sleep(1)
print ("Go!!!")
system('clear')

quizquestions = open('questions.txt','r')

score = 0
for q in quizquestions:
	
	qe = decrypt(q)
	question = qe.split("|")
	print (f"""{question[0]}
	""")
	options = question[3].split(",")
	for o in options:
		print (o)
	print (f"Score = {score}")
	print ("")
	answer = input ("Type your answer here: ")
	if answer == question[1]:
		print (f"Yay! you got it right. The answer was {question[2]}")
		score = score+1
	else:
		print (f"Oh dear!, The answer was actually {question[2]}")
	input ("Press the enter key when you are ready to continue...")
	system('clear')

print (f"Yay! You've finished the quiz {username}")
time.sleep(1)
print ("Your score was.....")
print (f"{score}/19")
print ("Well done!!")
exit()