side1 = int(input("Enter the first length: "))
side2 = int(input("Enter the second length: "))
side3 = int(input("Enter the last length: "))

if side1 > side2 and side1 > side3:
	hyp = side1
	a = side2
	b = side3
elif side2 > side1 and side2 > side3:
	hyp = side2
	a = side1
	b = side3
elif side3 > side1 and side3 > side2:
	hyp = side3
	a = side1
	b = side2
if a**2 + b**2 == hyp**2:
	print("These numbers are a pythagorian triplet.")
else:
	print("These numbers are not a pythagorian triplet.")