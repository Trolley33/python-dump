import time
#Iterate through 10 times
for o in range(0,11):
	i=10-o
	#If there are no bottles, print and do not continue
	if i == 0:
		print("No green bottles sitting on the wall.")
		break
	#If there is 1 bottle, set plural to false
	if i == 1:
		plural=False
	#Otherwise set plural to true
	else:
		plural=True
	#If there are multiple bottles, print pluralised version
	if plural:
		print("{0} Green bottles sitting on the wall, {0} green bottles sitting on the wall. And if one green bottle should accidentally fall, there'll be {1} green bottles, sitting on the wall.".format(i,i-1))
	#Otherwise print singular
	else:
		print("{0} Green bottle sitting on the wall, {0} green bottles sitting on the wall. And if one green bottle should accidentally fall, there'll be no green bottles, sitting on the wall.".format(i))
	time.sleep(1.5)