from random import randint
from random import SystemRandom
O00O000OOO00OO00000OO00 = 10
OOOOOOOOOO00O00O0O0O0OO = [36, 58, 1, 46, 23, 5, 16, 65, 2, 41, 2, 7, 1, 37,
    0, 11, 16, 2, 21, 16]
OO00O000O0O0O0OOO000OO0 = 'Decriptare.py'
if (OOOOOOOOOO00O00O0O0O0OO[4] ^ 3 - OOOOOOOOOO00O00O0O0O0OO[4]) % 3 == 0:
    OOOOOOOOOO00O00O0O0O0OO[5] = OOOOOOOOOO00O00O0O0O0OO[1
        ] * OOOOOOOOOO00O00O0O0O0OO[4] % OOOOOOOOOO00O00O0O0O0OO[11
        ] + OOOOOOOOOO00O00O0O0O0OO[6] % OOOOOOOOOO00O00O0O0O0OO[5]
    OOOOOOOOOO00O00O0O0O0OO[14] = randint(0, 100)
    OOOOOOOOOO00O00O0O0O0OO[4] = randint(0, 10) * OOOOOOOOOO00O00O0O0O0OO[11
        ] + OOOOOOOOOO00O00O0O0O0OO[8]
else:
    OOOOOOOOOO00O00O0O0O0OO[2] = randint(0, 100)
    OOOOOOOOOO00O00O0O0O0OO[5] = randint(0, 10) * OOOOOOOOOO00O00O0O0O0OO[11
        ] + OOOOOOOOOO00O00O0O0O0OO[8]
    if (OOOOOOOOOO00O00O0O0O0OO[1] + OOOOOOOOOO00O00O0O0O0OO[1] ^ 2) % 2 == 0:
        OOOOOOOOOO00O00O0O0O0OO[5] = OOOOOOOOOO00O00O0O0O0OO[1
            ] * OOOOOOOOOO00O00O0O0O0OO[4] % OOOOOOOOOO00O00O0O0O0OO[11
            ] + OOOOOOOOOO00O00O0O0O0OO[6] % OOOOOOOOOO00O00O0O0O0OO[5]
        OOOOOOOOOO00O00O0O0O0OO[14] = randint(0, 100)
        OOOOOOOOOO00O00O0O0O0OO[4] = randint(0, 10) * OOOOOOOOOO00O00O0O0O0OO[
            11] + OOOOOOOOOO00O00O0O0O0OO[8]
    else:
        OOOOOOOOOO00O00O0O0O0OO[2] = randint(0, 100)
        OOOOOOOOOO00O00O0O0O0OO[5] = randint(0, 10) * OOOOOOOOOO00O00O0O0O0OO[
            11] + OOOOOOOOOO00O00O0O0O0OO[8]
print('Inizio esecuzione ' + OO00O000O0O0O0OOO000OO0)
OO00O00O000OO000O0O0000 = 1
O00O0O0O000OO0OO0O0O0OO = input('Inserire un messaggio criptato: ')
OO00O00OO0OO0OOOOO00OOO = ''
OOO0OOOO00O0O0000OOOOOO = 0
OOO0O00OOO00O00OOO00O0O = len(O00O0O0O000OO0OO0O0O0OO)
while OO00O00O000OO000O0O0000 < 256:
    while OOO0OOOO00O0O0000OOOOOO < OOO0O00OOO00O00OOO00O0O:
        OO00O00OO0OO0OOOOO00OOO = OO00O00OO0OO0OOOOO00OOO + chr((ord(
            O00O0O0O000OO0OO0O0O0OO[OOO0OOOO00O0O0000OOOOOO]) -
            OO00O00O000OO000O0O0000) % 256)
        OOO0OOOO00O0O0000OOOOOO = OOO0OOOO00O0O0000OOOOOO + 1
    OO00O00OO0OO0OOOOO00OOO += '\n'
    OOO0OOOO00O0O0000OOOOOO = 0
    OO00O00O000OO000O0O0000 = OO00O00O000OO000O0O0000 + 1
print("Il messaggio decriptato e': " + OO00O00OO0OO0OOOOO00OOO)
print('Fine esecuzione')
