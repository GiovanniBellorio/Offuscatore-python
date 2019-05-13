#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import random

def main():

    print("--------------------------------------------------------------------------------")
    print("OBFUSCATION STARTED\n")

    name_src  = sys.argv[1]  # name of the source file, passed as argument
    name_dest = name_src+"_OBFUSCATE.py"  # name of the destination file

    file_SRC  = open(name_src, "r")
    file_DEST = open(name_dest, "w")

    file_mealy = open("mealy.py", "r")
    file_DEST.write(file_mealy.read())


    #### IMPLEMENTARE SEMPLICE PARSER SUGLI INPUT (testiamo su questa stringa come se fosse letta da file)
    #
    #
    #
    #
    string_input = "giovanni"
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

    # WRITE MEALY
    file_DEST.write("\n\n")
    file_DEST.write(("string_input = Mealy({},['0', '1'],['0', '1'],{},'q0')").format(states,transitions) + \
                   "\nprint(string_input.get_output_from_string('{}'))".format(new_string_input))


    print("\nOBFUSCATION ENDED")
    print("--------------------------------------------------------------------------------")


if __name__ == '__main__':
    main()
