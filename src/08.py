# This program adds up integers that have been passed as args in the com line
import sys
try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print('sum =', total)
except ValueError:
    print('Please supply integer arguments')
