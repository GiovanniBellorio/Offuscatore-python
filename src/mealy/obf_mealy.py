#!/usr/bin/python
# -*- coding: utf-8 -*-

import tokenize
import sys
from io import StringIO
import ast
import re
import random
import astor



class Mealy(object):
    #Mealy Machine : Finite Automata with Output

    def __init__(self, states, input_alphabet, output_alphabet, transitions, initial_state):
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
        return "Mealy(" + str(self.states) + "," + str(self.input_alphabet) + "," + str(self.output_alphabet) + "," + str(self.transitions) + ",'" + str(self.initial_state) + "')"

class MyVisitor(ast.NodeVisitor):

    def __init__(self, values, variable):
        self.values   = values
        self.variable = variable

    def visit_Str(self, node):
        self.values[self.variable] = "%s" % node.s

    def get_values(self, node):
        return self.values

class MyModifyValue(ast.NodeVisitor):

    def __init__(self, value):
        self.value = value

    def visit_Str(self, node):
        # DA SISTEMARE
        #
        #
        #
        node.s = (self.value)

def get_variables_values_string(tree):
    """
    :param tree:
    :return: a dictionary contains each variable (key) and its type (value) contains in the code (passed as AST 'tree')
    """
    variables = {}
    values = {}

    for node in ast.walk(tree):
        # Saved variables declared
        if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
            #if node.targets[0].id not in variables:
            if type(node.value).__name__ == "Str":
                variables[node.targets[0].id] = type(node.value).__name__
                values[node.targets[0].id] = ""
                
                MyVisitor(values, node.targets[0].id).visit(node)
                values = MyVisitor(values, node.targets[0].id).get_values(node)

    return variables, values

def rename_variables(tree, variables):
    # Rename names of variables used (general usage)
    i = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id in variables:
            if i != 0:
                node.id = variables[node.id]
            i += 1

    return tree

def rename_values(tree, values):
    # Rename values of variables used (general usage)
    for value in values:
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name) and type(node.value).__name__ == "Str":
                MyModifyValue(values[value]).visit(node)

    return tree

def mealy_machine(string_input):
    len_string_input = len(string_input)

    # create states
    iIdx = 0
    states = []
    for c in string_input:
        states.append('q'+str(iIdx))
        iIdx+=1

    # create transitions
    new_string_input = ''
    iIdx = 0
    transitions = {}
    for q in states:
        stato1 = random.randint(0,1)
        if stato1 == 0:
            stato2 = 1
        else:
            stato2 = 0
        new_string_input += str(stato1)
        char_random = random.randint(97,122)
        if (iIdx+1) == len_string_input:
            transitions.update({q:{str(stato1) : ('q0', ord(string_input[iIdx])), str(stato2) : ('q'+str(iIdx-1), char_random)}})
        elif (iIdx == 0):
            transitions.update({q:{str(stato1) : ('q'+str(iIdx+1), ord(string_input[iIdx])), str(stato2) : ('q'+str(len_string_input-1), char_random)}})
        else:
            transitions.update({q:{str(stato1) : ('q'+str(iIdx+1), ord(string_input[iIdx])), str(stato2) : ('q'+str(iIdx-1), char_random)}})
        iIdx+=1

    return Mealy(states,['0', '1'],['0', '1'],transitions,'q0')


def main():

    print("--------------------------------------------------------------------------------")
    print("OBFUSCATION STARTED\n")

    name_src  = sys.argv[1]  # name of the source file, passed as argument
    name_dest = name_src+"_OBFUSCATED.py"  # name of the destination file

    file_SRC  = open(name_src, "r")
    file_DEST = open(name_dest, "w")

    file_mealy = open("mealy.py", "r")
    file_DEST.write(file_mealy.read())
    file_DEST.write("\n\n")

    print("-> obfuscating variables with mealy")

    out = file_SRC.read()

    # Tree object contains the AST of the code
    tree = ast.parse(out)

    # Extraction of all variables defined
    variables, values = get_variables_values_string(tree)

    # mealy_machine
    new_values = {}
    for value in values:
        new_values[value] = mealy_machine(values[value])

    # Renomination of all variable occurrences
    tree = rename_values(tree, new_values)

    """
    # Define a new dict in order to bind variables-names with new-variables-names
    new_variables = {}
    # Choose new names
    for variable in variables:
        codice = "0000"
        new_variables[variable] = variable + ".get_output_from_string('%s')" % codice

    # Renomination of all variable occurrences
    tree = rename_variables(tree, new_variables)
    """

    out = astor.to_source(tree)


    print("\n")
    print(out)

    
    # Write the result into file_DEST
    file_DEST.write(out)

    print("\nOBFUSCATION ENDED")
    print("--------------------------------------------------------------------------------")


if __name__ == '__main__':
    main()
