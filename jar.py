#Sam Krimmel
#4/23/18
#jar.py - Precalc Project

from random import randint


N = 8 #int(input('Number of marbles, between 8 and 20: '))
W = 3 #int(input('Prize if correct guess, between 3 and 15: '))
runs = 100000
total = 0

for num in range(0,runs):
    
    Red = randint(0,N)
    Green = N-Red
    
    Pr = Red/N
    Pg = Green/N
    
    if Pg == 0:
        D = W
    else:
        D = (W*Pr)
    total += D
    
avg = total/runs


print('Red:',Red)
print('Green:',Green)
print('PR:',Pr)
print('PG:',Pg)
print('Price:',D)
print('Avg: ',avg)

