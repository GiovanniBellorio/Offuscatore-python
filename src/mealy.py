# -*- coding: utf-8 -*-
# pip3 install automata_python

class Mealy(object):
    """Mealy Machine : Finite Automata with Output """

    def __init__(self, states, input_alphabet, output_alphabet, transitions, initial_state):
        """
        6 tuple (Q, ∑, O, δ, X, q0) where −
        states is a finite set of states.
        alphabet is a finite set of symbols called the input alphabet.
        output_alphabet is a finite set of symbols called the output alphabet.
        transitions is the resultant data dictionary of input and output transition functions
        initial_state is the initial state from where any input is processed (q0 ∈ Q).
        """
        self.states = states
        self.input_alphabet = input_alphabet
        self.output_alphabet = output_alphabet
        self.transitions = transitions
        self.initial_state = initial_state

    def get_output_from_string(self, string):
        """Return Mealy Machine's output when a given string is given as input"""

        temp_list = list(string)
        current_state = self.initial_state
        output = ''
        for x in temp_list:
            output += chr(self.transitions[current_state][x][1])
            current_state = self.transitions[current_state][x][0]

        return output

    def __str__(self):
        output = "\nMealy Machine" + \
                 "\nStates " + str(self.states) + \
                 "\nTransitions " + str(self.transitions) + \
                 "\nInital State " + str(self.initial_state) + \
                 "\nInital Alphabet " + str(self.input_alphabet) + \
                 "\nOutput Alphabet" + str(self.output_alphabet)

        return output

#----------------------------------------------------------------------------------------------
string_input = "giovanni"
len_string_input = len(string_input)

# create states
iIdx = 0
states = []
for c in string_input:
	states.append('q'+str(iIdx))
	iIdx+=1

# create transitions
iIdx = 0
transitions = {}
for q in states:
	if (iIdx+1) == len_string_input:
		transitions.update({q:{'0' : ('q0', ord(string_input[iIdx]))}})
	else:
		transitions.update({q:{'0' : ('q'+str(iIdx+1), ord(string_input[iIdx]))}})
	iIdx+=1

mealy = Mealy(states,['0', '1'],['0', '1'],transitions,'q0')
#print(mealy)

new_string_input = ''
for c in string_input:
	new_string_input+='0'
print(mealy.get_output_from_string(new_string_input))
