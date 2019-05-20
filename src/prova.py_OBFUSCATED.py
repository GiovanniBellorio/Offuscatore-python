class Mealy(object):

    def __init__(self, states, input_alphabet, output_alphabet, transitions,
        initial_state):
        self.states = states
        self.input_alphabet = input_alphabet
        self.output_alphabet = output_alphabet
        self.transitions = transitions
        self.initial_state = initial_state

    def get_output_from_string(self, string):
        OO0O0OOOOOOO00OOOO = list(string)
        OO0OOOOOOO0OO0OOOO = self.initial_state
        O0O00OOO0OOO0000OO = ''
        for OO00OO0O0O00O00000 in OO0O0OOOOOOO00OOOO:
            O0O00OOO0OOO0000OO += chr(self.transitions[OO0OOOOOOO0OO0OOOO][
                OO00OO0O0O00O00000][1])
            OO0OOOOOOO0OO0OOOO = self.transitions[OO0OOOOOOO0OO0OOOO][
                OO00OO0O0O00O00000][0]
        return O0O00OOO0OOO0000OO


OOO00OO0OOOO000OOO = (
    "Mealy(['q0', 'q1', 'q2', 'q3', 'q4'],['0', '1'],['0', '1'],{'q0': {'1': ('q1', 75), '0': ('q4', 117)}, 'q1': {'0': ('q2', 101), '1': ('q0', 107)}, 'q2': {'0': ('q3', 118), '1': ('q1', 104)}, 'q3': {'0': ('q4', 105), '1': ('q2', 110)}, 'q4': {'1': ('q0', 110), '0': ('q3', 118)}},'q0')"
    )
OOO00OO0OOOO000OOO = eval(OOO00OO0OOOO000OOO).get_output_from_string('10001')
O0OOOO0O0OOO0OOOO0 = 0
OO00OO0O0O00O00000 = 3
if (OO00OO0O0O00O00000 + OO00OO0O0O00O00000 ^ 2) % 2 == 0:
    O0O000000OOOO000O0 = 0
for O0000O0O0000OO0OOO in range(0, 10):
    O0OOOO0O0OOO0OOOO0 += O0000O0O0000OO0OOO
O0000O0O0000OO0OOO = 10
if O0000O0O0000OO0OOO < 20:
    OO0O0OO00O000OOO0O = 3
print(OOO00OO0OOOO000OOO, O0OOOO0O0OOO0OOOO0)
if OOO00OO0OOOO000OOO == 'kevin':
    OOO00OO0OOOO000OOO = (
        "Mealy(['q0', 'q1'],['0', '1'],['0', '1'],{'q0': {'1': ('q1', 111), '0': ('q1', 110)}, 'q1': {'0': ('q0', 107), '1': ('q0', 104)}},'q0')"
        )
    OOO00OO0OOOO000OOO = eval(OOO00OO0OOOO000OOO).get_output_from_string('10')
else:
    OOO00OO0OOOO000OOO = 10
print(OOO00OO0OOOO000OOO)
