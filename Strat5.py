#Sam Krimmel
#4/27/18
#Strat4.py 

from random import randint

N = 10 #int(input('Number of marbles, between 8 and 20: '))
W = 8 #int(input('Prize if correct guess, between 3 and 15: '))
runs = 10000

#EXPERIMENTAL

EtotalWins = 0
EtotalRuns = 0

for i in range(0,runs):
    
    ERed = randint(0,N)
    EGreen = N-ERed
    
    EMarble = randint(1,N)
    
    if EMarble <= ERed:
        ERed -= 1
        EMarble2 = randint(1,(N-1))
    
    if (EMarble <= ERed and EMarble2 <= ERed and EMarble3 <= ERed) or (EMarble > ERed and EMarble2 > ERed+1 and EMarble3 > ERed+2):
        EtotalWins += 1
    elif (EMarble <= ERed and EMarble2 > ERed+1 and EMarble3 <= ERed) or (EMarble > ERed and EMarble2 <= ERed and EMarble3 <= ERed):
        EMarble4 = randint(1,N)
        if EMarble4 <= ERed:
            EtotalWins += 1
    elif (EMarble <= ERed and EMarble2 > ERed and EMarble3 > ERed) or (EMarble > ERed and EMarble2 <= ERed and EMarble3 > ERed):
        EMarble4 = randint(1,N)
        if EMarble4 > ERed:
            EtotalWins += 1
    EtotalRuns += 1

EPw = EtotalWins/EtotalRuns

print("Experimental Probability:", EPw)

#THEORETICAL

Ttotal = 0
TtotalProb = 0

for i in range(0,N+1):
    
    TRed = N - i
    TGreen = N - TRed
    
    TPr = TRed/N
    TPg = TGreen/N
    
    EPr_1 = (ERed-1)/(N-1)
    EPg_1 = (EGreen-1)/(N-1)
    
    EPr_2 = (ERed-2)/(N-2)
    EPg_2 = (EGreen-2)/(N-2)
    
    Ttotal += W*TPr
    
    TtotalProb += (TPr**3)+(TPg**3)+(2*(TPg*(TPr**3)))+(2*(TPr*(TPg**3)))

TDavg = Ttotal/(N+1)

TPw = TtotalProb/(N+1)

print("Theoretical Probability:", TPw)

R = (TPw*W)-TDavg

print("R: ",R)
