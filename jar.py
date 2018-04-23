#Sam Krimmel
#4/23/18
#jar.py - Precalc Project

from random import randint

N = int(input('Number of marbles, between 8 and 20: '))
w = int(input('Prize if correct guess, between 3 and 15: '))

Red = randint(0,N)
Green = N-Red

PR = Red/N
PG = Green/N

D = (-1*W*(PR))/(-1*(PG))

print(Red)
print(Green)
print(PR)
print(PG)
print(D)

