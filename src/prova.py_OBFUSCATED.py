class Mealy(object):

    def __init__(O00O00O0000O00O0O0O00O0, O00000O00OO0O0OO0O0O0O0,
        O0O000O0O0000O0OOO00OOO, O0O000OO0O00OOOO00OOOOO,
        OO00O000OO0OO0OOOOOOOOO, OOO000OOO000O0O00O00O0O):
        O00O00O0000O00O0O0O00O0.states = O00000O00OO0O0OO0O0O0O0
        O00O00O0000O00O0O0O00O0.input_alphabet = O0O000O0O0000O0OOO00OOO
        O00O00O0000O00O0O0O00O0.output_alphabet = O0O000OO0O00OOOO00OOOOO
        O00O00O0000O00O0O0O00O0.transitions = OO00O000OO0OO0OOOOOOOOO
        O00O00O0000O00O0O0O00O0.initial_state = OOO000OOO000O0O00O00O0O

    def O0O000000O0O0000OOOO0O0(OO0O000OOO00O00OOOOO0O0,
        O0O0O0O0000O00O00OOOOOO):
        OOOOO000O0000OO000O0OOO = list(O0O0O0O0000O00O00OOOOOO)
        O00OO0OOOOO0O00O000OO0O = OO0O000OOO00O00OOOOO0O0.initial_state
        O000OOO0OO0OO0OO0O00O00 = ''
        for OOOO0OOOO0O00O0O0O0O000 in OOOOO000O0000OO000O0OOO:
            O000OOO0OO0OO0OO0O00O00 += chr(OO0O000OOO00O00OOOOO0O0.
                transitions[O00OO0OOOOO0O00O000OO0O][
                OOOO0OOOO0O00O0O0O0O000][1])
            O00OO0OOOOO0O00O000OO0O = OO0O000OOO00O00OOOOO0O0.transitions[
                O00OO0OOOOO0O00O000OO0O][OOOO0OOOO0O00O0O0O0O000][0]
        return O000OOO0OO0OO0OO0O00O00


O00O00OO00O0OO000OO0OOO = (
    "Mealy(['q0', 'q1', 'q2', 'q3', 'q4'],['0', '1'],['0', '1'],{'q0': {'0': ('q1', 75), '1': ('q4', 119)}, 'q1': {'0': ('q2', 101), '1': ('q0', 98)}, 'q2': {'0': ('q3', 118), '1': ('q1', 122)}, 'q3': {'0': ('q4', 105), '1': ('q2', 111)}, 'q4': {'1': ('q0', 110), '0': ('q3', 97)}},'q0')"
    )
O00O00OO00O0OO000OO0OOO = eval(O00O00OO00O0OO000OO0OOO
    ).O0O000000O0O0000OOOO0O0('00001')
O00O0OO0OO0OOOO0OOO0O00 = 0
for OOO0OOO00OOO00O00OO00O0 in range(0, 10):
    O00O0OO0OO0OOOO0OOO0O00 += OOO0OOO00OOO00O00OO00O0
OOO0OOO00OOO00O00OO00O0 = 10
if OOO0OOO00OOO00O00OO00O0 < 20:
    O0000OO0O0O0O0O00OOOO00 = 3
    OOO0OOO00OOO00O00OO00O0 += O0000OO0O0O0O0O00OOOO00
print(O00O00OO00O0OO000OO0OOO, O00O0OO0OO0OOOO0OOO0O00)


def OO0OOO0OO00OO00O0O0O00O(O0OO00O00OOO0O000OOO00O, O0OO0OOOOO0OO0OOO0000O0):
    print('{} * {} = {}'.format(O0OO00O00OOO0O000OOO00O,
        O0OO0OOOOO0OO0OOO0000O0, O0OO00O00OOO0O000OOO00O *
        O0OO0OOOOO0OO0OOO0000O0))


OOOO0OOOO0O00O0O0O0O000 = 3
if (OOOO0OOOO0O00O0O0O0O000 + OOOO0OOOO0O00O0O0O0O000 ^ 2) % 2 == 0:
    O0O0000000O000O0O000O00 = 0
if O00O00OO00O0OO000OO0OOO == 'kevin':
    O00O00OO00O0OO000OO0OOO = (
        "Mealy(['q0', 'q1'],['0', '1'],['0', '1'],{'q0': {'1': ('q1', 111), '0': ('q1', 109)}, 'q1': {'1': ('q0', 107), '0': ('q0', 113)}},'q0')"
        )
    O00O00OO00O0OO000OO0OOO = eval(O00O00OO00O0OO000OO0OOO
        ).O0O000000O0O0000OOOO0O0('11')
else:
    O00O00OO00O0OO000OO0OOO = 10
print(O00O00OO00O0OO000OO0OOO)
print(OO0OOO0OO00OO00O0O0O00O(5, 6))
