#Sam Krimmel
#4/26/18
#Strat3.py

from random import randint

N = 8 #int(input('Number of marbles, between 8 and 20: '))
W = 8 #int(input('Prize if correct guess, between 3 and 15: '))
runs = 10000

#EXPERIMENTAL

EtotalWins = 0
EtotalRuns = 0

for i in range(0,runs):
    
    ERed = randint(0,N)
    EGreen = N-ERed
    
    EPr = ERed/N
    EPg = EGreen/N
    
    EMarble = randint(1,N)
    EMarble2 = randint(1,N)
    
    if (EMarble <= ERed and EMarble2 <= ERed) or (EMarble > ERed and EMarble2 > ERed):
        EtotalWins += 1
    EtotalRuns += 1

EPw = EtotalWins/EtotalRuns

print("Experimental Probability:", EPw)

#THEORETICAL

TtotalProb = 0

for i in range(0,N):
    
    TRed = N - i
    TGreen = N - TRed
    
    TPr = TRed/N
    TPg = TGreen/N
    
    TtotalProb += ((TPr**2) + (TPg**2))

TPw = TtotalProb/(N+1)

print("Theoretical Probability:", TPw)
    