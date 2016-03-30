__author__ = 'Reece'
import re


while 1:
    email = input("Enter your email: ")

    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Yes")
    else:
        print("No")