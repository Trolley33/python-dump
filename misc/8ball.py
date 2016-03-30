import random
import time
import sys
answers = ["Yes, I do think so!","I believe so.","Unlikely.","Ask again later.","I have to so no.","My sources say no.","Sure!"]
again=True
while(again):
	ui = input("Enter a question: ")
	print("\nThinking\n")
	time.sleep(2)
	answer = random.choice(answers)
	print(answer)
	ui = input("Do you wish to ask another question? Y/N\n")
	if ui.lower() == "N" or ui.lower() == "n":
		again=False