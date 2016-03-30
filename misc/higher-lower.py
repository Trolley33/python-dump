import random
wrong=True
print("I'm thinking of a number between 1 and 20, can you guess it?")
num = random.randint(1,20)
tries = 1
while(wrong):
	ui = input("Take a guess.\n")
	try:
		ui = int(ui)
	except ValueError:
		print("That's not a number!")
		continue
	if ui == num:
		print("Congrats, you have guessed my number in {0} guesses!".format(tries))
		wrong=False
		input("Press any key to continue...")
	elif ui > num:
		print("Too high!")
	elif ui < num:
		print("Too low!")
	tries+=1