def binary(number):
	currentDec = number
	while 1:
		currentBin = currentDec % 2
		currentDec = currentDec / 2
		binNum.append(int(currentBin))
		if currentDec == 0.5:
			break
		if currentBin:
			currentDec-=0.5

while 1:
	num = input("Enter a number: ")
	binNum = []
	if num == "exit":
		exit()
	if num == "0":
		print(0)
		continue
	try:
		num = int(num)
		binary(num)
		binNum.reverse()
		for i in binNum:
			print(i, end='')
		print("")
	except:
		print("That's not a number.")
