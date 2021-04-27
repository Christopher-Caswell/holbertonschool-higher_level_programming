#!/usr/bin/python3
import random
nmbr = random.randint(-10000, 10000)
if nmbr < 0:
    nimbr = nmbr * -1
else:
    nimbr = nmbr
l = nimbr % 10
if l > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(nmbr, l))
elif l == 0:
    print("Last digit of {:d} is {:d} and is 0".format(nmbr, l))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(nmbr, l))
