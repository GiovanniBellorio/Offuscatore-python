#!/usr/bin/python
# -*- coding: utf-8 -*-

import tokenize
import sys
from io import StringIO
import ast
import re
import random
from random import randint
from random import SystemRandom
import astor


# global set for random sequences generated
RANDOM_SEQUENCES_SET = set()


class MyVisitor(ast.NodeVisitor):

    def __init__(self, values, variable):
        self.values   = values
        self.variable = variable

    def visit_Str(self, node):
        self.values[self.variable] = "%s" % node.s

    def visit_Num(self, node):
        self.values[self.variable] = node.n

    def visit_List(self, node):
        tmp = []
        for idx, item in enumerate(node.elts):
            if idx:
                pass
            self.visit(item)
            tmp.append(self.values[self.variable])
        self.values[self.variable] = tmp

    def visit_Dict(self, node):
        tmp = {}
        for idx, (key, value) in enumerate(zip(node.keys, node.values)):
            if idx:
                pass
            self.visit(key)
            key_tmp = self.values[self.variable]
            self.visit(value)
            value_tmp = self.values[self.variable]
            tmp.update({key_tmp:value_tmp})
        self.values[self.variable] = tmp 

    def get_values(self, node):
        return self.values           


class MyModifyValue(ast.NodeVisitor):

    def __init__(self, value):
        self.value = value
    
    def visit_Str(self, node):
        node.s = self.value

    def visit_Num(self, node):
        print(self.value)
        node.n = self.value


def get_variables_values_Literal(tree):
    """
    :param tree:
    :return: a dictionary contains each variable (key) and its type (value) contains in the code (passed as AST 'tree')
    """
    variables = {}
    values = {}

    for node in ast.walk(tree):
        # Saved variables declared
        if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):

            if type(node.value).__name__ == "Str":
                variables[node.targets[0].id] = type(node.value).__name__
                values[node.targets[0].id] = ""
                
                MyVisitor(values, node.targets[0].id).visit(node)
                values = MyVisitor(values, node.targets[0].id).get_values(node)

            elif type(node.value).__name__ == "Num":
                variables[node.targets[0].id] = type(node.value).__name__
                values[node.targets[0].id] = 0
                
                MyVisitor(values, node.targets[0].id).visit(node)
                values = MyVisitor(values, node.targets[0].id).get_values(node)

            elif type(node.value).__name__ == "List":
                variables[node.targets[0].id] = type(node.value).__name__
                values[node.targets[0].id] = []
                
                MyVisitor(values, node.targets[0].id).visit(node)
                values = MyVisitor(values, node.targets[0].id).get_values(node)

            else:
                variables[node.targets[0].id] = type(node.value).__name__

    return variables, values


def isAssignStr(tree):
    values = {}

    for node in ast.walk(tree):
        # Saved variables declared
        if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
            if type(node.value).__name__ == "Str":
                return True

    return False


def isAssignInt(tree):
    values = {}

    for node in ast.walk(tree):
        # Saved variables declared
        if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
            if type(node.value).__name__ == "Num":
                return True

    return False


def isAssignList(tree):
    values = {}

    for node in ast.walk(tree):
        # Saved variables declared
        if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
            if type(node.value).__name__ == "List":
                return True

    return False


def rename_values_Literal(tree, values):
    # Rename values of variables used (general usage)
    for value in values:
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
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

    return "Mealy({},['0', '1'],['0', '1'],{},'q0')".format(states,transitions), new_string_input


def array_permutation(a):
    i = 1
    divisori = []
    while i <= len(a):
        if len(a) % i == 0:
            divisori.append(i)
        i += 1

    n = random.randint(1, 3000)
    i = 1
    divisori_n = []
    while i <= n:
        if n % i == 0:
            divisori_n.append(i)
        i += 1

    x = 0
    while x < len(divisori):
        div = divisori[x]

        if div in divisori_n and div != 1:
            n = random.randint(1, 3000)
            i = 1
            divisori_n = []
            while i <= n:
                if n % i == 0:
                    divisori_n.append(i)
                i += 1
            x = 0
        else:
            x += 1
            
    b = [ x*0 for x in range(0, len(a)) ]
    p = [ ((i-1)*n)%len(a) for i in range(0, len(a)) ]

    for i in range(0, len(a)):
        b[p[i]] = a[i]
    
    return b, p


def encoding_literal_data(out):
    class_mealy =   "#!/usr/bin/python\n\
# -*- coding: utf-8 -*-\n\n\
class Mealy(object):\n\
    def __init__(self, states, input_alphabet, output_alphabet, transitions, initial_state):\n\
        self.states = states\n\
        self.input_alphabet = input_alphabet\n\
        self.output_alphabet = output_alphabet\n\
        self.transitions = transitions\n\
        self.initial_state = initial_state\n\
    def get_output_from_string(self, string):\n\
        temp_list = list(string)\n\
        current_state = self.initial_state\n\
        output = ''\n\
        for x in temp_list:\n\
            output += chr(self.transitions[current_state][x][1])\n\
            current_state = self.transitions[current_state][x][0]\n\
        return output\n\n"

    def_encoding_integer = "def encoding_integer(digits):\n\
    num = 0\n\
    moltiplicatore = 1\n\
    for digit in digits:\n\
        num += digit*moltiplicatore\n\
        moltiplicatore *= 10\n\
    return num\n\n"

    print("-> obfuscating variables: str (mealy), int (permutation), array (permutation) ")

    # Tree object contains the AST of the code
    tree = ast.parse(out)
    tree_split = astor.to_source(tree).split("\n")
    tree = ""

    # indent tab
    indent = ""
    tab = "    "

    for subtree in tree_split:
        variables     = {}
        values        = {}
        new_values    = {}
        
        indent = ""

        try:
            while True:
                if "    " in subtree[0:4]:
                    subtree = subtree[4:len(subtree)]
                    indent += tab
                else:
                    break
            subtree = ast.parse(subtree)

        except:
            tree += indent + subtree + "\n"
            continue

        # Extraction of all variables defined
        variables, values = get_variables_values_Literal(subtree)

        # mealy_machine
        if isAssignStr(subtree):
            for value in values:
                new_values[value], codice = mealy_machine(values[value])

            # Renomination of all variable occurrences
            subtree = rename_values_Literal(subtree, new_values)

            for variable in variables:
                variable = variable

            tree += indent + astor.to_source(subtree) + indent + variable + " = eval(" + variable + ").get_output_from_string('%s')" % codice + "\n"

        # encoding_integer
        elif isAssignInt(subtree):
            for value in values:
                num = values[value]
                digits = []

                if num == 0:
                    digits.append(num)

                while num != 0:
                    digit = num % 10
                    num = int(num / 10)
                    digits.append(digit)

                new_values[value] = digits

            for variable in variables:
                variable = variable

            a = new_values[variable]
            b, p = array_permutation(a)

            tree += indent + variable + " = " + str(b) + "\n"
            tree += indent + variable + "_ooo = " + str(p) + "\n"
            tree += indent + variable + " = " + "encoding_integer([ " + variable + "[" + variable + "_ooo" + "[xxxxxxxxxxxx]] for xxxxxxxxxxxx in range(0, len(" + variable + ")) ])" + "\n"

        # encoding_list
        elif isAssignList(subtree):
            for value in values:
                a = values[value]

            for variable in variables:
                variable = variable

            b, p = array_permutation(a)

            tree += indent + variable + " = " + str(b) + "\n"
            tree += indent + variable + "_ooo = " + str(p) + "\n"
            tree += indent + variable + " = " + "[ " + variable + "[" + variable + "_ooo" + "[xxxxxxxxxxxx]] for xxxxxxxxxxxx in range(0, len(" + variable + ")) ]" + "\n"

        else:

            tree += indent + astor.to_source(subtree)

    return class_mealy + def_encoding_integer + tree


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
        new_variables[variable] = random_sequence()

    # Renomination of all variable occurrences
    tree = rename_variables(tree, new_variables)

    # Convert the new AST to a valid code
    return astor.to_source(tree)


def obfuscate_functions(out):
    """
        Returns 'source' with function def and call obfuscated.
    """
    print("-> obfuscating function definitions, body and call")

    # Tree object contains the AST of the code
    tree = ast.parse(out)

    critical_func_names = ["__init__", "__str__" , "__repr__", "main"]
    #critical_arg_names = ["self"]

    # -->  obfuscate definition and body
    functions = {}

    for node in ast.walk(tree):
        # Saved functions declared
        if isinstance(node, ast.FunctionDef):
            # save function name
            if node.name not in critical_func_names:
                # assign random name
                functions[node.name] = random_sequence()
                # change the name of def function (later also the occurrences in the code)
                node.name = functions[node.name]

            # Obfuscate arguments into the function def

            # dict for function arguments name
            arguments = {}
            # get argument list structure from node
            arguments_list = node.args.args
            # get the numbers of arguments
            num_arguments = len(arguments_list)

            # assign a new rand sequence for arg name and bind it with the old name
            for i in range(0, num_arguments):
                # --> NON SERVE FARE QUESTO CONTROLLO, FUNZIONA LO STESSO
                # if arguments_list[i].arg not in critical_arg_names:
                arguments[arguments_list[i].arg] = random_sequence()
                # assign the new random name at each argument between two parenthesis
                arguments_list[i].arg = arguments[arguments_list[i].arg]

            # rename arguments into body function
            rename_variables(node, arguments)

    # -->  obfuscate occurrences of various functions name

    for node in ast.walk(tree):
        # Saved functions declared
        if isinstance(node, ast.Call):
            # if "func" is instance of ast.Name and it has been previously defined, then change name
            if isinstance(node.func, ast.Name) and node.func.id in functions:
                node.func.id = functions[node.func.id]
            # if "func" is instance of ast.Attribute and it has been previously defined, then change name
            if isinstance(node.func, ast.Attribute) and node.func.attr in functions:
                node.func.attr = functions[node.func.attr]

    # Convert the new AST to a valid code
    return astor.to_source(tree)


def random_sequence():

    seq = generate_sequence()

    if seq not in RANDOM_SEQUENCES_SET:
        RANDOM_SEQUENCES_SET.add(seq)
        return seq

    else:
        random_sequence()


def generate_sequence():

    cryptorand = SystemRandom()

    sequence = []

    for i in range(22):
        flip = random.randint(1, 2)
        if flip == 1:
            sequence.append("0")
        else:
            sequence.append("O")

    random.seed()
    cryptorand.shuffle(sequence)

    return "O"+"".join(sequence)


def opaque_predicate(out):

    print("-> opaque_predicate")

    # first opaque predicate
    pred1 = """
x = 3
if(x + x^2) % 2 == 0:
    index = 0
"""

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

    #
    out = opaque_predicate(out)

    #
    out = encoding_literal_data(out)

    # Call 'obfuscate_variables()' function
    out = obfuscate_variables(out)

    out = obfuscate_functions(out)

    # Write the result into file_DEST
    file_DEST.write(out)
    file_DEST.close()
    file_SRC.close()

    print("\nOBFUSCATION ENDED")
    print("--------------------------------------------------------------------------------")


if __name__ == '__main__':
    main()
