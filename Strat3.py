#Sam Krimmel
#4/26/18
#Strat3.py

from random import randint

N = 10 #int(input('Number of marbles, between 8 and 20: '))
W = 8 #int(input('Prize if correct guess, between 3 and 15: '))
runs = 1000000

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
    
    if EMarble == EMarble2:
        EtotalWins += 1
    EtotalRuns += 1

EPw = EtotalWins/EtotalRuns

print(EtotalWins)
print(EtotalRuns)
print(EPw)