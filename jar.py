#Sam Krimmel
#4/23/18
#jar.py - Precalc Project

from random import randint


N = 10 #int(input('Number of marbles, between 8 and 20: '))
W = 8 #int(input('Prize if correct guess, between 3 and 15: '))
runs = 10000

total = 0

#EXPERIMENTAL

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
PwTotal = 0

#THEORETICAL

Ttotal = 0

for i in range(0,N):
    TRed = N - i
    TGreen = N - TRed
    TPr = TRed/N
    TPg = TGreen/N
    
    Ttotal += W*TPr
    PwTotal += (TPr**2) + (TPg**2)
    
PwAvg = PwTotal/(N+1)
Tavg = Ttotal/(N+1)

print('Experimental Average Price ($D):',avg)
print('Theoretical Average Price ($D):',Tavg)

#STRATEGY 3:

PlAvg = 1 - PwAvg

P = (PwAvg*W)-Tavg
print(PwAvg)
print(P)

