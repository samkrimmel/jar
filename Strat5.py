#Sam Krimmel
#4/27/18
#Strat4.py 

from random import randint

W = int(input('Prize if correct guess, between 3 and 15: '))
N = int(input('Number of marbles, between 8 and 20: '))
runs = int(input('Experimental runs: '))

#EXPERIMENTAL

Etotal = 0
EtotalWins = 0
EtotalRuns = 0

for i in range(0,runs):
    
    marbles = []
    
    result = ''

    ERed = randint(0,N)
    EGreen = N - ERed
    
    marbles = ['R']*ERed + ['G']*EGreen
    
    EPr = marbles.count('R')/len(marbles)
    
    marbles2 = list(marbles)
    
    Emarble = randint(0,N-1)
    result += str(marbles[Emarble])

    Emarble2 = randint(0,N-1)
    while Emarble == Emarble2:
        Emarble2 = randint(0,N-1)
    result += str(marbles[Emarble2])
    
    if result == 'RR' or result == 'GG':
        Emarble3 = randint(0,N-1)
        result += str(marbles[Emarble3])
        
    else:
        Emarble3 = randint(0,N-1)
        while Emarble3 == Emarble2 or Emarble3 == Emarble:
            Emarble3 = randint(0,N-1)
        result += str(marbles2[Emarble3])
        
        Emarble4 = randint(0,N-1)
        result += str(marbles[Emarble4])

    if result == 'RRR' or result == 'RGRR' or result == 'RGGG' or result == 'GGG' or result == 'GRRR' or result == 'GRGG':
        EtotalWins += 1
    EtotalRuns += 1
    
    Etotal += W*EPr
    
EDavg = Etotal/runs

print(EtotalWins)
print(EtotalRuns)
EPw = EtotalWins/EtotalRuns

ES = (EPw*W)-EDavg

print("Experimental S: ",ES)

#THEORETICAL

Ttotal = 0
TtotalProb = 0

for i in range(0,N+1):
    
    TRed = N - i
    TGreen = N - TRed
    
    TPr = TRed/N
    TPg = TGreen/N
    
    TPr_r = (TRed-1)/(N-1)
    if TPr_r < 0:
        TP_r = 0
    
    TPg_g = (TGreen-1)/(N-1)
    if TPg_g < 0:
        TPg_g = 0
    
    TPr_g = (TRed)/(N-1)
    if TPr_g < 0:
        TPr_g = 0
    
    TPg_r = (TGreen)/(N-1)
    if TPg_r < 0:
        TPg_r = 0
        
    TPr_rg = (TRed-1)/(N-2)
    if TPr_rg < 0:
        TPr_rg = 0
    
    TPg_rg = (TGreen-1)/(N-2)
    if TPg_rg < 0:
        TPg_rg = 0
    
    
    Ttotal += W*TPr
    
    TtotalProb += (TPr*TPr_r*TPr)+(TPg*TPg_g*TPg)+(TPr*TPg_r*TPg_rg*TPg)+(TPg*TPr_g*TPr_rg*TPr)+(TPg*TPr_g*TPg_rg*TPg)+(TPr*TPg_r*TPr_rg*TPr)

TDavg = Ttotal/(N+1)

TPw = TtotalProb/(N+1)

TS = (TPw*W)-TDavg

print("Theoretical S: ",TS)
