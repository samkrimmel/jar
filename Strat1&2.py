#Sam Krimmel
#4/23/18
#jar.py - Precalc Project

from random import randint


N = int(input('Number of marbles, between 8 and 20: '))
W = int(input('Prize if correct guess, between 3 and 15: '))
runs = int(input('Experimental Runs: '))

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
        ED = (W*EPr)
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

