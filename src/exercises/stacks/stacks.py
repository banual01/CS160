from typing import Union

from pythonds3.basic import Stack


class StackError(Exception):
    """Stack errors"""

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class TokenError(Exception):
    """Token errors"""

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


def rev_string(my_str: str):
    # Return str
    """Reverse characters in a string using a stack"""
    str_stack = Stack()
    for char in my_str:
        str_stack.push(char)
    reverse_str = ""
    for rchar in range(len(my_str)):
        reverse_str += str_stack.pop()
    
    return reverse_str

def par_checker(line: str):
    """Textbook implementation"""
    # Return boolean
    stack = Stack()
    balanced = True
    i = 0
    while i < len(line) and balanced:
        symbol = line[i]
        if symbol == "(":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                stack.pop()
        i = i + 1
    return balanced and stack.is_empty()


def par_checker_ext(line: str):
    # Return boolean
    """Check if parentheses are balanced"""
    stack = Stack()
    open_symbol = {"(":1, "{":2, "[":3, "<":4}
    end_symbol = {")":1, "}":2, "]":3, ">":4}
    balanced = True
    i = 0
    while i < len(line) and balanced:
        symbol = line[i]
        if symbol in open_symbol:
            stack.push(symbol)
        elif symbol in end_symbol:
            if stack.is_empty():
                balanced = False
            else:
                if end_symbol[symbol] == open_symbol[stack.peek()]: 
                    stack.pop()
                else:
                    balanced = False
        i += 1
    return balanced and stack.is_empty()

def par_checker_file(filename: str):
    """Check expressions in the file"""
    with open(filename,"r") as r:
        inputcase = r.readlines()
        for line in inputcase:
            line = line[:-1]
            if par_checker_ext(line):
                print(f"{line} is balanced")
            else:
                print(f"{line} is NOT balanced")

def base_converter(dec_num: int, base: int):
    # Return str
    """Convert a decimal number to any base"""
    acceptable_base = [2,8,16]
    new_string = ""
    if base in acceptable_base:
        digits = "0123456789ABCDEF"
        rem_stack = Stack()

        while dec_num > 0:
            rem = dec_num % base
            rem_stack.push(rem)
            dec_num = dec_num // base

        while not rem_stack.is_empty():
            new_string = new_string + digits[rem_stack.pop()]

    if new_string == "":
        raise ValueError(f"Cannot convert to base {base}.")
    else:
        return f"{new_string}"
        


def rpn_calc(postfix_expr: str):
    # Return Union[int, float]
    """Evaluate a postfix expression"""
    stack = Stack()
    for str_index in range(len(postfix_expr)):
        if  "number" == int:
            stack.push()
        elif "operations" == "+" and "-" and "*" and "/":
            operand1 = stack.pop()[0]
            operand2 = stack.pop()[1]
            stack.push(do_math("operation",operand1,operand2)) 



def do_math(operation: str, operand1: Union[int, float], operand2: Union[int, float]):
    """Evaluate a mathematical operation"""
    if operation == "+":
        return operand1 + operand2
    elif operation == "-":
        return operand1 - operand2
    elif operation == "*":
        return operand1 * operand2
    elif operation == "/":
        return operand1 / operand2                    
