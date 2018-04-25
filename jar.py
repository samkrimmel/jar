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

#THEORETICAL

Ttotal = 0
TPrTotal = 0
TPgTotal = 0

for i in range(0,N):
    TRed = N - i
    TGreen = N - TRed
    TPr = TRed/N
    TPg = TGreen/N
    
    Ttotal += W*TPr
    TPrTotal += TPr
    TPgTotal += TPg
    
TPrAvg = TPrTotal/(N+1)
TPgAvg = TPgTotal/(N+1)
Tavg = Ttotal/(N+1)

print('Experimental Average Price ($D):',avg)
print('Theoretical Average Price ($D):',Tavg)

#STRATEGY 3:

Pw = (TPrAvg**2) + (TPgAvg**2)
Pl = 1 - Pw

print(TPrAvg)
print(TPgAvg)
print(Pw)

P = (Pw*W)-Tavg

print(P)

