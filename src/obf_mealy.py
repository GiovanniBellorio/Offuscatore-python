#!/usr/bin/python
# -*- coding: utf-8 -*-

import tokenize
import sys
from io import StringIO
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
    file_DEST.write("\n\n")


    #### IMPLEMENTARE SEMPLICE PARSER SUGLI INPUT (testiamo su questa stringa come se fosse letta da file)
    variabili = {}
    source = file_SRC.read()
    io_obj = StringIO(source)

    for tok in tokenize.generate_tokens(io_obj.readline):
        token_type = tok[0]
        token_string = tok[1]
        start_line, start_col = tok[2]
        end_line, end_col = tok[3]
        ltext = tok[4]

        if token_type == 3: # il type STRING è 3
            ltext = ltext.replace(" ", "")
            name_var = ""
            for i in ltext:
                if i == '=':
                    break
                name_var += i

            string_input = token_string
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
            variabili[name_var] = new_string_input
            file_DEST.write(("Mealy({},['0', '1'],['0', '1'],{},'q0')").format(states,transitions))

        elif token_type == 1 and token_string != "print": # il type NAME è 1 
            ltext = ltext.replace(" ", "")
            if "=" in ltext:
                file_DEST.write(token_string)
                continue
            else:
                file_DEST.write("{}.get_output_from_string('{}')".format(token_string,variabili[token_string]))

        else:
            file_DEST.write(token_string)

    print(variabili)
    print("\nOBFUSCATION ENDED")
    print("--------------------------------------------------------------------------------")


if __name__ == '__main__':
    main()
