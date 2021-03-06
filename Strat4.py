#Sam Krimmel
#4/27/18
#Strat4.py 

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
    EMarble3 = randint(1,N)
    
    if (EMarble <= ERed and EMarble2 <= ERed and EMarble3 <= ERed) or (EMarble > ERed and EMarble2 > ERed and EMarble3 > ERed):
        EtotalWins += 1
    elif (EMarble <= ERed and EMarble2 > ERed and EMarble3 <= ERed) or (EMarble > ERed and EMarble2 <= ERed and EMarble3 <= ERed):
        EMarble4 = randint(1,N)
        if EMarble4 <= ERed:
            EtotalWins += 1
    elif (EMarble <= ERed and EMarble2 > ERed and EMarble3 > ERed) or (EMarble > ERed and EMarble2 <= ERed and EMarble3 > ERed):
        EMarble4 = randint(1,N)
        if EMarble4 > ERed:
            EtotalWins += 1
    EtotalRuns += 1

EDavg = Etotal/(runs)

EPw = EtotalWins/EtotalRuns

ER = (EPw*W)-EDavg

print("Experimental Probability:", EPw)

print("Experimental R: ", ER)

#THEORETICAL

Ttotal = 0
TtotalProb = 0

for i in range(0,N+1):
    
    TRed = N - i
    TGreen = N - TRed
    
    TPr = TRed/N
    TPg = TGreen/N
    
    Ttotal += W*TPr
    
    TtotalProb += (TPr**3)+(TPg**3)+(2*(TPg*(TPr**3)))+(2*(TPr*(TPg**3)))

TDavg = Ttotal/(N+1)

TPw = TtotalProb/(N+1)

print("Theoretical Probability:", TPw)

TR = (TPw*W)-TDavg

print("Theoretical R: ",TR)
