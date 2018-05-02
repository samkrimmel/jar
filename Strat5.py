#Sam Krimmel
#4/27/18
#Strat4.py 

from random import randint

W = 8 #int(input('Prize if correct guess, between 3 and 15: '))
runs = 1000

#EXPERIMENTAL

EtotalWins = 0
EtotalRuns = 0

for i in range(0,runs):
    
    N = 10 #int(input('Number of marbles, between 8 and 20: '))
    
    marbles = []
    
    result = ''

    for n in range(1,N+1):
        mcolor = randint(1,2)
        if mcolor == 1:
            marbles.append('G')
        else:
            marbles.append('R')

    Emarble = randint(0,N-1)
    result += str(marbles[Emarble])
    N -= 1
    del marbles[Emarble]
    
    Emarble2 = randint(0,N-1)
    result += str(marbles[Emarble2])
    N -= 1
    del marbles[Emarble2]

    Emarble3 = randint(0,N-1)
    result += str(marbles[Emarble3])
    N -= 1
    del marbles[Emarble3]

    Emarble4 = randint(0,N-1)
    result += str(marbles[Emarble4])
    N -= 1
    del marbles[Emarble4]

    if result == 'RRRR' or result == 'RRRG' or result == 'RGRR' or result == 'RGGG' or result == 'GGGG' or result == 'GGGR' or result == 'GRRR' or result == 'GRGG':
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
    
    TPr_1 = (TRed-1)/(N-1)
    TPg_1 = (TGreen-1)/(N-1)
    
    TPr_2 = (TRed-2)/(N-2)
    TPg_2 = (TGreen-2)/(N-2)
    
    TPr_3 = (TRed-3)/(N-3)
    TPg_3 = (TGreen-3)/(N-3)
    
    Ttotal += W*TPr
    
    TtotalProb += (TPr*TPr_1*TPr_2)+(TPg*TPg_1*TPg_2)+(2*(TPg_3*(TPr*TPr_1*TPr_2)))+(2*(TPr_3*(TPg*TPg_1*TPg_2)))

TDavg = Ttotal/(N+1)

TPw = TtotalProb/(N+1)

print("Theoretical Probability:", TPw)

R = (TPw*W)-TDavg

print("R: ",R)
