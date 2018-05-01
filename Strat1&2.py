#Sam Krimmel
#4/23/18
#jar.py - Precalc Project

from random import randint


N = 10 #int(input('Number of marbles, between 8 and 20: '))
W = 8 #int(input('Prize if correct guess, between 3 and 15: '))
runs = 10000

Etotal = 0

#STRATEGIES 1&2

#EXPERIMENTAL

for num in range(0,runs):
    
    ERed = randint(0,N)
    EGreen = N-ERed
    
    EPr = ERed/N
    EPg = EGreen/N
    
    if EPg == 0:
        ED = W
    else:
        ED = (W*Pr)
    Etotal += ED
    
EDavg = Etotal/runs
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

TDavg = Ttotal/(N+1)

PwAvg = PwTotal/(N+1)


print('Experimental Average Price ($D):',EDavg)
print('Theoretical Average Price ($D):',TDavg)

#STRATEGY 3:

PlAvg = 1 - PwAvg

P = (PwAvg*W)-TDavg
print(PwAvg)
print(P)
