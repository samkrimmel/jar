#Sam Krimmel
#4/23/18
#jar.py - Precalc Project

from random import randint


N = 19 #int(input('Number of marbles, between 8 and 20: '))
W = 7 #int(input('Prize if correct guess, between 3 and 15: '))
runs = 100000

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

for i in range(0,N):
    TRed = N - i
    TGreen = N - TRed
    TPr = TRed/N
    TPg = TGreen/N
    
    Ttotal += W*TPr

Tavg = Ttotal/(N+1)

print('Experimental Average Price ($D):',avg)
print('Theoretical Average Price ($D):',Tavg)

#STRATEGY 3:

Pw = (Pr**2) + (Pg**2)
Pl = 1 - Pw

P = ((Pw*W)-(Pw*D)-(Pl*D))/(Pw+Pl)

print(P)

