import sys
import time
for i in range(1,100):
	if 100-i>1:
		plural="bottles"
	else:
		plural="bottle"
	print("{0} {1} of beer on the wall, {0} {1} of beer, take one down, pass it around and there's {2} {1} of beer on the wall.".format(100-i,plural,99-i))
	time.sleep(2)