from random import randint
from random import SystemRandom
O000O0OO0OO0O0O00OO00O0 = 10
OOOO0OOOOOO00O0O0OOO00O = [36, 58, 1, 46, 23, 5, 16, 65, 2, 41, 2, 7, 1, 37,
    0, 11, 16, 2, 21, 16]
from datetime import *
import random
OOOO00O00O0OOOOOO00O0OO = 'MergeSort.py'
print('Inizio esecuzione di ' + OOOO00O00O0OOOOOO00O0OO)


def OO0000O0O00000OOO00OOO0(O0000000O0OO0O0O0O0OO0O):
    O0O000O000OO0O00OO0O0OO = []
    O0O00O00O0O00OO0O0O0O0O = 0
    for O0O00O00O0O00OO0O0O0O0O in range(0, O0000000O0OO0O0O0O0OO0O):
        O0O000O000OO0O00OO0O0OO.append(int(random.random() * 100 + 1))
    return O0O000O000OO0O00OO0O0OO


def O0O000000O000O0OO0O0OOO(O0000OOO0OOO000OOOOO000, OO000O0000000OO0OO0O000):
    OOOO00OOO0OO000O0OOOOOO = []
    O0OOO0O0OO00O0O00OOOO00 = 0
    O0000O0OO000O00O000O00O = 0
    while O0OOO0O0OO00O0O00OOOO00 < len(O0000OOO0OOO000OOOOO000
        ) and O0000O0OO000O00O000O00O < len(OO000O0000000OO0OO0O000):
        if O0000OOO0OOO000OOOOO000[O0OOO0O0OO00O0O00OOOO00
            ] < OO000O0000000OO0OO0O000[O0000O0OO000O00O000O00O]:
            OOOO00OOO0OO000O0OOOOOO.append(O0000OOO0OOO000OOOOO000[
                O0OOO0O0OO00O0O00OOOO00])
            O0OOO0O0OO00O0O00OOOO00 += 1
        else:
            OOOO00OOO0OO000O0OOOOOO.append(OO000O0000000OO0OO0O000[
                O0000O0OO000O00O000O00O])
            O0000O0OO000O00O000O00O += 1
    while O0OOO0O0OO00O0O00OOOO00 < len(O0000OOO0OOO000OOOOO000):
        OOOO00OOO0OO000O0OOOOOO.append(O0000OOO0OOO000OOOOO000[
            O0OOO0O0OO00O0O00OOOO00])
        O0OOO0O0OO00O0O00OOOO00 += 1
        if 7 + OOOO0OOOOOO00O0O0OOO00O[4] ^ 2 - 1 != OOOO0OOOOOO00O0O0OOO00O[5
            ] ^ 2:
            OOOO0OOOOOO00O0O0OOO00O[5] = OOOO0OOOOOO00O0O0OOO00O[1
                ] * OOOO0OOOOOO00O0O0OOO00O[4] % OOOO0OOOOOO00O0O0OOO00O[11
                ] + OOOO0OOOOOO00O0O0OOO00O[6] % OOOO0OOOOOO00O0O0OOO00O[5]
            OOOO0OOOOOO00O0O0OOO00O[14] = randint(0, 100)
            OOOO0OOOOOO00O0O0OOO00O[4] = randint(0, 10
                ) * OOOO0OOOOOO00O0O0OOO00O[11] + OOOO0OOOOOO00O0O0OOO00O[8]
        else:
            OOOO0OOOOOO00O0O0OOO00O[2] = randint(0, 100)
            OOOO0OOOOOO00O0O0OOO00O[5] = randint(0, 10
                ) * OOOO0OOOOOO00O0O0OOO00O[11] + OOOO0OOOOOO00O0O0OOO00O[8]
    while O0000O0OO000O00O000O00O < len(OO000O0000000OO0OO0O000):
        OOOO00OOO0OO000O0OOOOOO.append(OO000O0000000OO0OO0O000[
            O0000O0OO000O00O000O00O])
        O0000O0OO000O00O000O00O += 1
    return OOOO00OOO0OO000O0OOOOOO


def OOOO0000O0OO0OOO0O0OO0O(O0000O0000OO00O00OO0OO0):
    OO000O0000000OO0OO0O000 = []
    if OOOO0OOOOOO00O0O0OOO00O[4
        ] ^ O000O0OO0OO0O0O00OO00O0 - OOOO0OOOOOO00O0O0OOO00O[5
        ] ^ O000O0OO0OO0O0O00OO00O0 % OOOO0OOOOOO00O0O0OOO00O[4
        ] - OOOO0OOOOOO00O0O0OOO00O[5]:
        OOOO0OOOOOO00O0O0OOO00O[5] = OOOO0OOOOOO00O0O0OOO00O[1
            ] * OOOO0OOOOOO00O0O0OOO00O[4] % OOOO0OOOOOO00O0O0OOO00O[11
            ] + OOOO0OOOOOO00O0O0OOO00O[6] % OOOO0OOOOOO00O0O0OOO00O[5]
        OOOO0OOOOOO00O0O0OOO00O[14] = randint(0, 100)
        OOOO0OOOOOO00O0O0OOO00O[4] = randint(0, 10) * OOOO0OOOOOO00O0O0OOO00O[
            11] + OOOO0OOOOOO00O0O0OOO00O[8]
    else:
        OOOO0OOOOOO00O0O0OOO00O[2] = randint(0, 100)
        OOOO0OOOOOO00O0O0OOO00O[5] = randint(0, 10) * OOOO0OOOOOO00O0O0OOO00O[
            11] + g[8]
    OOOO00OOO0OO000O0OOOOOO = []
    if len(O0000O0000OO00O00OO0OO0) > 1:
        OOO000O00000OO0O0O00000 = int(len(O0000O0000OO00O00OO0OO0) / 2)
        for O0O00O00O0O00OO0O0O0O0O in range(0, OOO000O00000OO0O0O00000):
            OO000O0000000OO0OO0O000.append(O0000O0000OO00O00OO0OO0[
                O0O00O00O0O00OO0O0O0O0O])
        for O0O00O00O0O00OO0O0O0O0O in range(OOO000O00000OO0O0O00000, len(
            O0000O0000OO00O00OO0OO0)):
            OOOO00OOO0OO000O0OOOOOO.append(O0000O0000OO00O00OO0OO0[
                O0O00O00O0O00OO0O0O0O0O])
        OOOO000OO0OOO0OO00OO0O0 = OOOO0000O0OO0OOO0O0OO0O(
            OO000O0000000OO0OO0O000)
        OOOOOO000OOOOOO0OOOOOOO = OOOO0000O0OO0OOO0O0OO0O(
            OOOO00OOO0OO000O0OOOOOO)
        OO000000O0O000000O0OOO0 = O0O000000O000O0OO0O0OOO(
            OOOO000OO0OOO0OO00OO0O0, OOOOOO000OOOOOO0OOOOOOO)
        return OO000000O0O000000O0OOO0
    if len(O0000O0000OO00O00OO0OO0) == 1:
        return O0000O0000OO00O00OO0OO0


O0O00O0OOO0OOOO0OOOO0O0 = True
if O0O00O0OOO0OOOO0OOOO0O0 == True:
    O0O0OOOOOO0O00O00OO0000 = int(input('Inserisci numero elementi vettore: '))
    O00OOOO0OOO0O0O0O00000O = OO0000O0O00000OOO00OOO0(O0O0OOOOOO0O00O00OO0000)
    OOO00OOO000OOO0O0O00000 = [3, 5]
    O0O00OOOO0OO00000O0OOOO = [7, 12, 15]
if O0O00O0OOO0OOOO0OOOO0O0 == False:
    OOO00OOO000OOO0O0O00000 = [3, 5]
    O0O00OOOO0OO00000O0OOOO = [7, 12, 15]
O00O000OO0OO0O00O0OO000 = datetime.utcnow()
if __name__ == '__main__':
    if O0O00O0OOO0OOOO0OOOO0O0 == True:
        print('Lista:      ' + str(O00OOOO0OOO0O0O0O00000O))
    O0O000O0OO000OO00OOOOO0 = O0O000000O000O0OO0O0OOO(OOO00OOO000OOO0O0O00000,
        O0O00OOOO0OO00000O0OOOO)
    O0000O0OO0OO0OOOO000O0O = OOOO0000O0OO0OOO0O0OO0O(O00OOOO0OOO0O0O0O00000O)
O0OO000000OO0OO0O0OO000 = datetime.utcnow()
print('MergeSort:  ' + str(O0000O0OO0OO0OOOO000O0O))
print('')
print('Fusione di due liste ordinate:')
print('')
print('Lista1:     ' + str(OOO00OOO000OOO0O0O00000))
print('Lista2:     ' + str(O0O00OOOO0OO00000O0OOOO))
print('Merge:      ' + str(O0O000O0OO000OO00OOOOO0))
OO0000O000OO00O0OO00OO0 = O0OO000000OO0OO0O0OO000 - O00O000OO0OO0O00O0OO000
print(OO0000O000OO00O0OO00OO0)
print('Esecuzione terminata')
