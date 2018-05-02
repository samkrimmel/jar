#Sam Krimmel
#4/27/18
#Strat4.py 

from random import randint

W = 8 #int(input('Prize if correct guess, between 3 and 15: '))
N = 10 #int(input('Number of marbles, between 8 and 20: '))
runs = 1000 #int(input('Experimental runs: '))

#EXPERIMENTAL

Etotal = 0
EtotalWins = 0
EtotalRuns = 0

for i in range(0,runs):
    
    marbles = []
    
    result = ''

    for n in range(1,N+1):
        mcolor = randint(1,2)
        if mcolor == 1:
            marbles.append('G')
        else:
            marbles.append('R')
    
    EPr = marbles.count('R')/len(marbles)
    
    marbles2 = list(marbles)
    
    Emarble = randint(0,N-1)
    result += str(marbles[Emarble])
    N -= 1
    del marbles2[Emarble]
    
    Emarble2 = randint(0,N-1)
    result += str(marbles[Emarble2])
    N -= 1
    del marbles2[Emarble2]
    
    if result == 'RR' or result == 'GG':
        N += 2
        Emarble3 = randint(0,N-1)
        result += str(marbles[Emarble3])
    else:
        Emarble3 = randint(0,N-1)
        result += str(marbles2[Emarble3])
        N -= 1
        del marbles2[Emarble3]
        
        N += 3
        Emarble4 = randint(0,N-1)
        result += str(marbles[Emarble4])

    if result == 'RRR' or result == 'RGRR' or result == 'RGGG' or result == 'GGG' or result == 'GRRR' or result == 'GRGG':
        EtotalWins += 1
    EtotalRuns += 1
    
    Etotal += W*EPr
    
EDavg = Etotal/runs

EPw = EtotalWins/EtotalRuns

ER = (EPw*W)-EDavg

print("Experimental R: ",ER)

print("Experimental Probability:", EPw)

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

print("Theoretical Probability:", TPw)

TR = (TPw*W)-TDavg

print("Theoretical R: ",TR)
