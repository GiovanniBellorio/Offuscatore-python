#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
from random import SystemRandom
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

class Encoding():
    def integer(self,digits):
        num = 0
        moltiplicatore = 1
        for digit in digits:
            num += digit*moltiplicatore
            moltiplicatore *= 10
        return num

i = [1, 0]
i_ooo = [1, 0]
i = Encoding().integer([ i[i_ooo[xxxxxxxxxxxx]] for xxxxxxxxxxxx in range(0, len(i)) ])
print(i)
class Employee:
    def __init__(self, a_name, a_salary):
        self.name = a_name
        self.salary = a_salary
    def displayCount(self):
        empCount = [0]
        empCount_ooo = [0]
        empCount = Encoding().integer([ empCount[empCount_ooo[xxxxxxxxxxxx]] for xxxxxxxxxxxx in range(0, len(empCount)) ])
        print('Total Employee %d' % Employee.empCount)
    def displayEmployee(self):
        print('Name : ', self.name, ', Salary: ', self.salary)
g = [58, 0, 65, 36, 37, 16, 16, 1, 5, 21, 7, 23, 2, 2, 46, 16, 41, 1, 11, 2]
g_ooo = [3, 0, 17, 14, 11, 8, 5, 2, 19, 16, 13, 10, 7, 4, 1, 18, 15, 12, 9, 6]
g = [ g[g_ooo[xxxxxxxxxxxx]] for xxxxxxxxxxxx in range(0, len(g)) ]
if (g[1] + g[1] ^ 2) % 2 == 0:
    g[5] = g[1] * g[4] % g[11] + g[6] % g[5]
    g[14] = randint(0, 100)
    g[4] = randint(0, 10) * g[11] + g[8]
else:
    g[2] = randint(0, 100)
    g[5] = randint(0, 10) * g[11] + g[8]
emp1 = Employee('Zara', 2000)
emp1.displayEmployee()
