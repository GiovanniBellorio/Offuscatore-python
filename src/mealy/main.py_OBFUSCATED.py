#!/usr/bin/python
# -*- coding: utf-8 -*-

class Mealy(object):
    #Mealy Machine : Finite Automata with Output

    def __init__(self, states, input_alphabet, output_alphabet, transitions, initial_state):
        '''
        6 tuple (Q, ∑, O, δ, X, q0) where −
        states is a finite set of states.
        alphabet is a finite set of symbols called the input alphabet.
        output_alphabet is a finite set of symbols called the output alphabet.
        transitions is the resultant data dictionary of input and output transition functions
        initial_state is the initial state from where any input is processed (q0 ∈ Q).
        '''
        self.states = states
        self.input_alphabet = input_alphabet
        self.output_alphabet = output_alphabet
        self.transitions = transitions
        self.initial_state = initial_state

    def get_output_from_string(self, string):
        #Return Mealy Machine's output when a given string is given as input

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

pippo = <__main__.Mealy object at 0x104c670f0>
print(pippo)
