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

VARIABLES_DICT = dict()


class MyVisitor(ast.NodeVisitor):

    def __init__(self, values, variable):
        self.values   = values
        self.variable = variable

    def visit_Name(self, node):
        self.values[self.variable] = node.id

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

    # Create states
    iIdx = 0
    states = []
    for c in string_input:
        states.append('q'+str(iIdx))
        iIdx+=1

    # Create transitions
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

    return "xxxxxMxxxxx({},['0', '1'],['0', '1'],{},'q0')".format(states,transitions), new_string_input


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

    # Code for Mealy decoding
    class_mealy =   "#!/usr/bin/python\n\
# -*- coding: utf-8 -*-\n\n\
from random import randint\n\
from random import SystemRandom\n\
class xxxxxMxxxxx(object):\n\
    def __init__(self, some_states, a_input_alphabet, a_output_alphabet, some_transitions, a_initial_state):\n\
        self.xxsxxtxxaxxtxxexxsxx = some_states\n\
        self.xxixxnxxpxxuxxtxx_xxaxxlxxpxxhxxaxxbxxexxtxx = a_input_alphabet\n\
        self.xxoxxuxxtxxpxxuxxtxx_xxaxxlxxpxxhxxaxxbxxexxtxx = a_output_alphabet\n\
        self.xxtxxrxxaxxnxxsxxixxtxxixxoxxnxxsxx = some_transitions\n\
        self.xxixxnxxixxtxxixxaxxlxx_xxsxxtxxaxxtxxexx = a_initial_state\n\
    def get_output_from_string(self, string):\n\
        temp_list = list(string)\n\
        current_state = self.xxixxnxxixxtxxixxaxxlxx_xxsxxtxxaxxtxxexx\n\
        output = ''\n\
        for x in temp_list:\n\
            output += chr(self.xxtxxrxxaxxnxxsxxixxtxxixxoxxnxxsxx[current_state][x][1])\n\
            current_state = self.xxtxxrxxaxxnxxsxxixxtxxixxoxxnxxsxx[current_state][x][0]\n\
        return output\n\n"

    # Code for permutation encoding
    def_encoding_integer = "class xxxxxExxxxx():\n\
    def integer(self,digits):\n\
        num = 0\n\
        moltiplicatore = 1\n\
        for xxxxxDxxxxx in digits:\n\
            num += xxxxxDxxxxx*moltiplicatore\n\
            moltiplicatore *= 10\n\
        return num\n\n"

    """
        Returns 'source' with obfuscation of array with permutation, string with mealy machine and number with permutation.
    """

    print("-> obfuscating variables: str (mealy), int (permutation), array (permutation) ")

    # Tree object contains the AST of the code
    tree = ast.parse(out)
    tree_split = astor.to_source(tree).split("\n")
    tree = ""

    # Indent tab
    indent = ""
    tab = "    "

    # For each row in code
    for subtree in tree_split:
        variables     = {}
        values        = {}
        new_values    = {}
        
        # Count tab indent position
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

        # If string:
        if isAssignStr(subtree):

            # start mealy_machine and save new value
            for value in values:
                new_values[value], codice = mealy_machine(values[value])

            # Renomination of all variable occurrences
            subtree = rename_values_Literal(subtree, new_values)

            for variable in variables:
                variable = variable

            # Decode function for mealy machine
            tree += indent + astor.to_source(subtree) + indent + variable + " = eval(" + variable + ").get_output_from_string('%s')" % codice + "\n"

        # If integer:
        elif isAssignInt(subtree):

            # Encoding integer
            for value in values:
                num = values[value]

                # Extract the digits of number
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

            # Create permutation of digits
            a = new_values[variable]
            b, p = array_permutation(a)

            # Decode function for permutation digits
            tree += indent + variable + " = " + str(b) + "\n"
            tree += indent + variable + "_ooo = " + str(p) + "\n"
            tree += indent + variable + " = " + "xxxxxExxxxx().integer([ " + variable + "[" + variable + "_ooo" + "[xxxxxxxxxxxx]] for xxxxxxxxxxxx in range(0, len(" + variable + ")) ])" + "\n"

        # If array:
        elif isAssignList(subtree):

            # Encoding list
            for value in values:
                a = values[value]

            for variable in variables:
                variable = variable

            # Create permutation of position array
            b, p = array_permutation(a)

            # Decode funcyion for permutation position
            tree += indent + variable + " = " + str(b) + "\n"
            tree += indent + variable + "_ooo = " + str(p) + "\n"
            tree += indent + variable + " = " + "[ " + variable + "[" + variable + "_ooo" + "[xxxxxxxxxxxx]] for xxxxxxxxxxxx in range(0, len(" + variable + ")) ]" + "\n"

        # Else:
        else:

            tree += indent + astor.to_source(subtree)

    # Return definition class Mealy, function encoding for permutation and tree
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
        if isinstance(node, ast.Attribute) and (node.value == "self"):
        #if isinstance(node, ast.Attribute) and (node.value.id == "self"):
                variables[node.attr] = type(node.attr).__name__
    return variables


def rename_variables(tree, variables):
    # Rename names of variables used (general usage)
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id in variables:
            node.id = variables[node.id]
        if isinstance(node, ast.Attribute) and node.attr in variables:
            node.attr = variables[node.attr]

    return tree
#ClassDef(name='Employee', bases=[], keywords=[], body=[Assign(targets=[Name(id='empCount', ctx=Store())], value=Num(n=0)), FunctionDef(name='__init__', args=arguments(args=[arg(arg='self', annotation=None), arg(arg='name', annotation=None), arg(arg='salary', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='name', ctx=Store())], value=Name(id='name', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='salary', ctx=Store())], value=Name(id='salary', ctx=Load())), AugAssign(target=Attribute(value=Name(id='Employee', ctx=Load()), attr='empCount', ctx=Store()), op=Add(), value=Num(n=1))], decorator_list=[], returns=None), FunctionDef(name='displayCount', args=arguments(args=[arg(arg='self', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[BinOp(left=Str(s='Total Employee %d'), op=Mod(), right=Attribute(value=Name(id='Employee', ctx=Load()), attr='empCount', ctx=Load()))], keywords=[]))], decorator_list=[], returns=None), FunctionDef(name='displayEmployee', args=arguments(args=[arg(arg='self', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Str(s='Name : '), Attribute(value=Name(id='self', ctx=Load()), attr='name', ctx=Load()), Str(s=', Salary: '), Attribute(value=Name(id='self', ctx=Load()), attr='salary', ctx=Load())], keywords=[]))], decorator_list=[], returns=None)], decorator_list=[])
#Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='salary', ctx=Store())])

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
        VARIABLES_DICT[variable] = random_sequence()


    # Renomination of all variable occurrences
    tree = rename_variables(tree, VARIABLES_DICT)

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
                # se il nome è un omonimo di una variabile già scovata in precedenza, allora uso quello
                if arguments_list[i].arg in VARIABLES_DICT:
                    arguments[arguments_list[i].arg] = VARIABLES_DICT[arguments_list[i].arg]
                # altrimenti, assegno un nome a caso
                else:
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
    """
        Returns 'source' with opaque predicate.
    """

    print("-> opaque_predicate")

    # Opaque predicate 1
    pred1 = "if(xxgxx[3] % xxgxx[5] == xxgxx[2]):\n\
    xxgxx[5] = (xxgxx[1] * xxgxx[4]) % xxgxx[11] + xxgxx[6]% xxgxx[5]\n\
    xxgxx[14] = randint(0, 100)\n\
    xxgxx[4] = randint(0, 10) * xxgxx[11] + xxgxx[8]\n\
else: \n\
    xxgxx[6] = randint(0, 10) * xxgxx[5] + xxgxx[2]\n\
"
    
    # Opaque predicate 2
    pred2 = "if(xxgxx[7] % xxgxx[11] == xxgxx[8]):\n\
    xxgxx[11] = (xxgxx[4] + xxgxx[7] + xxgxx[10]) % xxgxx[11] + xxgxx[3] % xxgxx[5]\n\
    xxgxx[17] = randint(0, 100)\n\
    xxgxx[6] = randint(0, 10) * xxgxx[5] + xxgxx[2]\n\
else:\n\
    xxgxx[4] = randint(0, 10) * xxgxx[11] + xxgxx[8]\n\
"

    # Tree object contains the AST of the code
    tree = ast.parse(out)
    tree_split = astor.to_source(tree).split("\n")
    tree = ""

    # Indent tab
    indent = ""
    tab = "    "

    num_row = 0
    # For each row in code
    for subtree in tree_split:

        if subtree == "":
            continue

        # Count tab indent position
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
            
            # Extend a loop condition
            if "while" in subtree[0:5]:
                guardia = subtree[5:len(subtree)-1]
                tree += indent + "while (xxgxx[1] + xxgxx[1]^2) % 2 == 0 and" + guardia + ":\n"
            
            # Extend a if condition
            elif "if" in subtree[0:2]:
                guardia = subtree[2:len(subtree)-1]
                tree += indent + "if (xxgxx[1] + xxgxx[1]^2) % 2 == 0 and" + guardia + ":\n"
            
            else:
                tree += indent + subtree + "\n"
            
            continue
        
        # The simplest block splitting
        if (num_row % 2 == 0): # block red
            tree += indent + astor.to_source(subtree) + "\n"
        
        else: # block blue

            number = randint(1, 2)
            predicate = 'pred' + str(number)

            # Add indent to predicate
            predicate_split = eval(predicate).split("\n")
            predicate = ""

            num_row_predicate = 0
            for line in predicate_split:
                predicate += indent + line + "\n"

                if (num_row_predicate == 2):
                    predicate += indent + "    " + astor.to_source(subtree)
                num_row_predicate += 1

            tree += predicate

        num_row += 1
    
    # Return out with library random and array of number for opaque predicate
    out = '''from random import randint
from random import SystemRandom
xxnxx = 10
xxgxx = [36,58,1,46,23,5,16,65,2,41,2,7,1,37,0,11,16,2,21,16]\n''' + tree

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

    # Call 'opaque_predicate()' function
    out = opaque_predicate(out)

    # Call 'encoding_literal_data()' function
    out = encoding_literal_data(out)

    # Call 'obfuscate_variables()' function
    out = obfuscate_variables(out)
    
    # Call 'obfuscate_functions()' function
    out = obfuscate_functions(out)

    # Write the result into file_DEST
    file_DEST.write(out)
    file_DEST.close()
    file_SRC.close()

    print("\nOBFUSCATION ENDED")
    print("--------------------------------------------------------------------------------")


if __name__ == '__main__':
    main()
