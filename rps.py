import random
import math
ok = 0

for lol in range(1,100):
    huma = 0
    compu = 0
    while huma <= 2 and compu <= 2 :

        # cho = input("enter your choice: [(r)ock, (p)aper, (s)cissors]")
        cho = random.choice(['r','p','s'])
        # cho = cho.lower()

        comp = random.choice(['r','p','s'])

        if comp == cho:
            #print("hey it is draw \n" )
            ok += ok
        elif (cho == "r" and comp == "s") or (cho == "p" and comp == "r") or (cho == "s" and comp == "p"):
            #print("1st one has won \n")
            huma += 1
        else:
            #print("second one has won \n")
            compu += 1

    if huma == 3 :
        print("human has won")
    elif compu == 3:
        print("the computer has won")
