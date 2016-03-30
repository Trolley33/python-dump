import time
import sys

def numb(number):
	if i==1:
		return "st"
	if i==2:
		return "nd"
	if i==3:
		return "rd"
	else:
		return "th"

for i in range(1,13):
	numberSuffix = numb(i)
	print("On the {0}{1} day of christmas, my true love gave to me:".format(i,numberSuffix))
	if i >= 12:
		print("12 Drummers Drumming")
	if i >=11:
		print("11 Pipers Piping")
	if i >=10:
		print("10 Lords a Leaping")
	if i>=9:
		print("9 Ladies Dancing")
	if i>=8:
		print("8 Maids a Milking")
	if i>=7:
		print("7 Swans a Swimming")
	if i>=6:
		print("6 Geese a Laying")
	if i>=5:
		print("5 Golden Rings")
	if i>=4:
		print("4 Calling Birds")
	if i>=3:
		print("3 French Hens")
	if i>=2:
		print("2 Turtle Doves")
	if i>1:
		print("And a Partridge in a Pear Tree")
	if i==1:
		print("A Partridge in a Pear Tree")
	time.sleep(5)