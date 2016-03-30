__author__ = 'Reece'

import time

i = 3

primes = [2]
div = True

left = True

while 1:
    for prime in primes:
        if i % prime == 0:
            div = True
            break
        else:
            div = False
        if i**(1/2) >= prime:
            break

    if not div:
        primes.append(i)
        if left:
            print("{} is prime.".format(i), end=' ')
            left = False
        else:
            print("{} is prime.".format(i))
            left = True

    i += 1