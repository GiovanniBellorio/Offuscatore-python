#!/usr/bin/python
# -*- coding: utf-8 -*-

class Mealy(object):
    def __init__(self, some_states, a_input_alphabet, a_output_alphabet, some_transitions, a_initial_state):
        self.states = some_states
        self.input_alphabet = a_input_alphabet
        self.output_alphabet = a_output_alphabet
        self.transitions = some_transitions
        self.initial_state = a_initial_state
    def get_output_from_string(self, string):
        temp_list = list(string)
        current_state = self.initial_state
        output = ''
        for x in temp_list:
            output += chr(self.transitions[current_state][x][1])
            current_state = self.transitions[current_state][x][0]
        return output

def encoding_integer(digits):
    num = 0
    moltiplicatore = 1
    for digit in digits:
        num += digit*moltiplicatore
        moltiplicatore *= 10
    return num

from random import randint
from random import SystemRandom
g = [58, 23, 65, 2, 37, 16, 16, 1, 5, 2, 7, 0, 2, 36, 46, 16, 41, 1, 11, 21]
g_ooo = [13, 0, 7, 14, 1, 8, 15, 2, 9, 16, 3, 10, 17, 4, 11, 18, 5, 12, 19, 6]
g = [ g[g_ooo[xxxxxxxxxxxx]] for xxxxxxxxxxxx in range(0, len(g)) ]
class Employee:
    empCount = [0]
    empCount_ooo = [0]
    empCount = encoding_integer([ empCount[empCount_ooo[xxxxxxxxxxxx]] for xxxxxxxxxxxx in range(0, len(empCount)) ])
    def __init__(self, a_name, a_salary):
        self.name = a_name
        self.salary = a_salary
        Employee.empCount += 1
    def displayCount(self):
        print('Total Employee %d' % Employee.empCount)
    def displayEmployee(self):
        print('Name : ', self.name, ', Salary: ', self.salary)
if (g[1] + g[1] ^ 2) % 2 == 0:
    g[5] = g[1] * g[4] % g[11] + g[6] % g[5]
    g[14] = randint(0, 100)
    g[4] = randint(0, 10) * g[11] + g[8]
else:
    g[2] = randint(0, 100)
    g[5] = randint(0, 10) * g[11] + g[8]
print(g)
emp1 = Employee('Zara', 2000)
emp1.displayEmployee()
