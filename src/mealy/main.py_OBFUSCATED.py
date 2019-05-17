#!/usr/bin/python
# -*- coding: utf-8 -*-

class Mealy(object):
    def __init__(self, states, input_alphabet, output_alphabet, transitions, initial_state):
        self.states = states
        self.input_alphabet = input_alphabet
        self.output_alphabet = output_alphabet
        self.transitions = transitions
        self.initial_state = initial_state
    def get_output_from_string(self, string):
        temp_list = list(string)
        current_state = self.initial_state
        output = ''
        for x in temp_list:
            output += chr(self.transitions[current_state][x][1])
            current_state = self.transitions[current_state][x][0]
        return output

pippo = (
    "Mealy(['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7'],['0', '1'],['0', '1'],{'q0': {'0': ('q1', 103), '1': ('q7', 104)}, 'q1': {'1': ('q2', 105), '0': ('q0', 102)}, 'q2': {'0': ('q3', 111), '1': ('q1', 97)}, 'q3': {'1': ('q4', 118), '0': ('q2', 102)}, 'q4': {'1': ('q5', 97), '0': ('q3', 115)}, 'q5': {'1': ('q6', 110), '0': ('q4', 99)}, 'q6': {'0': ('q7', 110), '1': ('q5', 116)}, 'q7': {'1': ('q0', 105), '0': ('q6', 119)}},'q0')"
    )
print(eval(pippo).get_output_from_string('01011101'))
