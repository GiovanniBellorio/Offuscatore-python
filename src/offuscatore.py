#!/usr/bin/python
# -*- coding: utf-8 -*-

import tokenize
import sys
from io import StringIO
import ast
import re
import random
from random import randint
import astor



def remove_comments_and_docstrings(source):
    """
    Returns 'source' minus comments and docstrings.
    """
    # Function taken from pyminifier project: https://github.com/liftoff/pyminifier

    print("-> removing comments and docstrings")

    io_obj = StringIO(source)
    out = ""
    prev_toktype = tokenize.INDENT
    last_lineno = -1
    last_col = 0
    myline = ""
    is_junk = False

    for tok in tokenize.generate_tokens(io_obj.readline):
        token_type = tok[0]
        token_string = tok[1]
        start_line, start_col = tok[2]
        end_line, end_col = tok[3]
        ltext = tok[4]
        # The following two conditionals preserve indentation.
        # This is necessary because we're not using tokenize.untokenize()
        # (because it spits out code with copious amounts of oddly-placed
        # whitespace).
        if start_line > last_lineno:
            last_col = 0
        if start_col > last_col:
            myline += (" " * (start_col - last_col))
        # Remove comments:
        if token_type == tokenize.COMMENT:
            is_junk = True
            pass
        # This series of conditionals removes docstrings:
        elif token_type == tokenize.STRING:
            if prev_toktype != tokenize.INDENT:
        # This is likely a docstring; double-check we're not inside an operator:
                if prev_toktype != tokenize.NEWLINE:
                    # Note regarding NEWLINE vs NL: The tokenize module
                    # differentiates between newlines that start a new statement
                    # and newlines inside of operators such as parens, brackes,
                    # and curly braces.  Newlines inside of operators are
                    # NEWLINE and newlines that start new code are NL.
                    # Catch whole-module docstrings:
                    if start_col > 0:
                        # Unlabelled indentation means we're inside an operator
                        myline += token_string
                    # Note regarding the INDENT token: The tokenize module does
                    # not label indentation inside of an operator (parens,
                    # brackets, and curly braces) as actual indentation.
                    # For example:
                    # def foo():
                    #     "The spaces before this docstring are tokenize.INDENT"
                    #     test = [
                    #         "The spaces before this string do not get a token"
                    #     ]
                    else:
                        is_junk = True
                else:
                    is_junk = True
            else:
                is_junk = True

        else:
            myline += token_string

        if token_type == tokenize.NEWLINE or token_type == tokenize.NL:
            if not (is_junk and re.match(r'^\s*$', myline)):
                out += myline
            myline = ""
            is_junk = False

        prev_toktype = token_type
        last_col = end_col
        last_lineno = end_line
    return out


def get_variables(tree):
    """
    :param tree:
    :return: a dictionary contains each variable (key) and its type (value) contains in the code (passed as AST 'tree')
    """

    variables = {}

    for node in ast.walk(tree):
        # Saved variables declared
        if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
                if node.targets[0].id not in variables:
                    variables[node.targets[0].id] = type(node.value).__name__

    return variables

def rename_variables(tree, variables):
    # Rename names of variables used (general usage)
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id in variables:
            node.id = variables[node.id]

    return tree


def rand_sequence():
    sequence = "O"
    coin = ('0', 'O')

    for i in range(17):
        flip = random.choice(coin)
        sequence += flip

    return sequence


def obfuscate_variables(out):
    """
        Returns 'source' with variables offuscated.
    """

    print("-> obfuscating variables")

    # Tree object contains the AST of the code
    tree = ast.parse(out)

    # Extraction of all variables defined
    variables = get_variables(tree)

    # Define a new dict in order to bind variables-names with new-variables-names
    new_variables = {}
    # Choose new names
    for variable in variables:
        new_variables[variable] = rand_sequence()

    # Renomination of all variable occurrences
    tree = rename_variables(tree, new_variables)

    # Convert the new AST to a valid code
    return astor.to_source(tree)


def opaque_predicate(out):

    # first opaque predicate
    pred1 = "x = 3\nif(x + x^2) % 2 == 0:\n\tindex = 0"

    # set a flag to False
    flag = False

    # check a position where to insert the opaque predicate
    # the position is choiced randomly and it can't be insert
    # after a row that finish with ':'
    while (flag == False):
        try:
            pos = randint(0, len(out))
            if(out[pos] == '\n' and out[pos-1] != ':'):
                flag = True
        except IndexError as error:
            # Output expected IndexErrors.
            print("string index out of range")

    
    # insert the opaque predicate
    out = out[:pos] + '\n' + pred1 + out[pos:]
    pos+= len(pred1) + 3

    return out


def main():

    print("--------------------------------------------------------------------------------")
    print("OBFUSCATION STARTED\n")

    name_src = sys.argv[1]  # name of the source file, passed as argument
    name_dest = name_src+"_OBFUSCATED.py"  # name of the destination file

    file_SRC = open(name_src, "r")
    file_DEST = open(name_dest, "w")

    # Call 'remove_comments_and_docstrings()' function on the source file object
    # which it is first converted to a string through the read() method.
    out = remove_comments_and_docstrings(file_SRC.read())   # 'out' contains a string with the entire code

    out = opaque_predicate(out)

    # Call 'obfuscate_variables()' function
    out = obfuscate_variables(out)

    # Write the result into file_DEST
    file_DEST.write(out)


    print("\nOBFUSCATION ENDED")
    print("--------------------------------------------------------------------------------")



if __name__ == '__main__':
    main()
