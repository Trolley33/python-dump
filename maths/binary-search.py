__author__ = 'Reece'

target = int(input("Number between 1 and 100: "))

lower_b = 1
upper_b = 100
midpoint = 50
while midpoint != target:
    midpoint = int((upper_b + lower_b) / 2)
    if target > midpoint:
        lower_b = midpoint
        print("higher {}".format(midpoint))
    else:
        upper_b = midpoint
        print("lower {}".format(midpoint))