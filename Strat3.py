#Sam Krimmel
#4/26/18
#Strat3.py

from random import randint

N = int(input('Number of marbles, between 8 and 20: '))
W = int(input('Prize if correct guess, between 3 and 15: '))
runs = int(input('Experimental Runs: '))

#EXPERIMENTAL

Etotal = 0
EtotalWins = 0
EtotalRuns = 0

for i in range(0,runs):
    
    ERed = randint(0,N)
    EGreen = N-ERed
    
    EPr = ERed/N
    EPg = EGreen/N
    
    Etotal += W*EPr
    
    EMarble = randint(1,N)
    EMarble2 = randint(1,N)
    
    if (EMarble <= ERed and EMarble2 <= ERed) or (EMarble > ERed and EMarble2 > ERed):
        EtotalWins += 1
    EtotalRuns += 1

EDavg = Etotal/runs

EPw = EtotalWins/EtotalRuns

EP = (EPw*W)-EDavg

print("Experimental P: ",EP)

#THEORETICAL

Ttotal = 0
TtotalProb = 0

for i in range(0,N+1):
    
    TRed = N - i
    TGreen = N - TRed
    
    TPr = TRed/N
    TPg = TGreen/N
    
    Ttotal += W*TPr
    
    TtotalProb += ((TPr**2) + (TPg**2))

TDavg = Ttotal/(N+1)

TPw = TtotalProb/(N+1)

TP = (TPw*W)-TDavg

print("Theoretical P: ",TP)
    
