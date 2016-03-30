import random
import os
again = True
while(again):
	clear = lambda: os.system('cls')
	clear()
	alive=True
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	wordList = [['r','e','e','c','e'],['b','l','a','k','e'],['j','o','e'],['a','l','p','h','a','b','e','t'],['h','a','n','g','m','a','n'],['s','u','n','d','a','y'],['j','a','z','z'],['d','a','z'],['l','o','u','i','s','e'],['s','u','k','i'],['d','o','g'],['b','r','a','n','d','o','n'],['m','i','c','k','e','y'],['r','o','o','n','e','y'],['b','i','l','l'],['c','h','r','i','s','t','m','a','s']]
	y = random.randint(0,len(wordList)-1)
	word = wordList[y]
	def hang(fails):
		global alive
		if(fails==1):
			#---1st---#
			print("\n     |      \n     |      \n     |      \n     |       \n     |      \n     |\n    _|___")
		if(fails==2):
			#---2nd---#
			print("      _______\n     |      \n     |      \n     |      \n     |       \n     |      \n     |\n    _|___")
		if(fails==3):
			#---3rd---#
			print("      _______\n     |/      \n     |      \n     |      \n     |       \n     |      \n     |\n    _|___")
		if(fails==4):
			#---4th---#
			print("      _______\n     |/      |\n     |      \n     |      \n     |       \n     |      \n     |\n    _|___")
		if(fails==5):
			#---5th---#
			print("      _______\n     |/      |\n     |      (_)\n     |      \n     |       \n     |      \n     |\n    _|___")
		if(fails==6):
			#---6th---#
			print("      _______\n     |/      |\n     |      (_)\n     |       |\n     |       |\n     |      \n     |\n    _|___")
		if(fails==7):
			#---7th---#
			print("      _______\n     |/      |\n     |      (_)\n     |      \|\n     |       |\n     |      \n     |\n    _|___")
		if(fails==8):
			#---8th---#
			print("      _______\n     |/      |\n     |      (_)\n     |      \|/\n     |       |\n     |      \n     |\n    _|___")
		if(fails==9):
			#---9th---#
			print("      _______\n     |/      |\n     |      (_)\n     |      \|/\n     |       |\n     |      / \n     |\n    _|___")
		if(fails==10):
			#---Fully hanged---#
			print("      _______\n     |/      |\n     |      (_)\n     |      \|/\n     |       |\n     |      / \ \n     |\n    _|___")
			alive=False
			input("You have died, the word was {0}.".format(word))
	wrongs=0
	guessed=[]
	display = "_ "*len(word)

	while(alive):
		if "".join(word) == display.replace(" ", ""):
			input("You have guessed correctly, the word was {0}, congrats!".format("".join(word)))
			break
		print("You have these letters to choose from.")
		for a in alphabet:
			if a not in guessed:
				print(a,' ', end="")
		print(" ")
		print(display)
		userInput = input(">> ").lower()
		if userInput in alphabet and userInput not in guessed:
			guessed.append(userInput)
			if userInput in word:
				display = " ".join([char if char in guessed else "_" for char in word])
			else:
				wrongs+=1
				hang(wrongs)
		else:
			print("That is not a letter in your options.")
