#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    nimbr = number * -1
    l = (nimbr % 10) * -1
else:
    nimbr = number
    l = nimbr % 10
n = number
if l > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(n, l))
elif l == 0:
    print("Last digit of {:d} is {:d} and is 0".format(n, l))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(n, l))
