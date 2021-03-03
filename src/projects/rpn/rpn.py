#!/usr/bin/env python3
"""
Project `rpn` implementation

@author:
"""

from pythonds3.basic import Stack


class StackError(Exception):
    """Stack errors"""

    def __init__(self, *args, **kwargs):
        """Initializer"""
        Exception.__init__(self, *args, **kwargs)


class TokenError(Exception):
    """Token errors"""

    def __init__(self, *args, **kwargs):
        """Initializer"""
        Exception.__init__(self, *args, **kwargs)



def postfix_eval(postfix_expr: str) -> int:
    # TODO: Evaluate an expression
    operation = {"+", "-", "*", "/", "%", "**", "//"}
    equal = {"="}
    eval_stack = postfix_expr
    math_stack = Stack()
    for str_index in range(len(eval_stack)):
        if eval_stack[str_index] not in operation and eval_stack[str_index] not in equal:
            try:
                int(eval_stack[str_index])
                float(eval_stack[str_index])
                Number = int(eval_stack[str_index])
                math_stack.push(Number)
            except:
                raise TokenError(f"Unknown token: {eval_stack[str_index]}")
        elif eval_stack[str_index] in equal:
            print(math_stack.peek())
            return math_stack.peek()
        else: 
            try:
                op2 = math_stack.pop()
                op1 = math_stack.pop()
                math_stack.push(do_math(eval_stack[str_index], op1, op2))
                
            except:
                raise StackError("Stack is empty")    
    if math_stack.size() > 1:
        raise StackError("Stack is not empty")
print(postfix_eval)




def do_math(op: str, op1: int, op2: int) -> int:
    # TODO: Process arithmetic operations
    try:
        print(type(op1))
        type(op1) == int
        type(op2) == int
        type(op) == str
    except:
        raise SyntaxError("invalid syntax")
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "*":
        return op1 * op2
    elif op == "%":
        try:
            op1 % op2    
            return op1 % op2
        except:
            raise ZeroDivisionError("integer division or modulo by zero")
    elif op == "//":
        try:
            op1 // op2
            return op1 // op2
        except:
            raise ZeroDivisionError("integer division or modulo by zero")
    elif op == "**":
        return op1 ** op2
    elif op == "/":
        try:
            op1 / op2
            print(op1 / op2)
            return op1 / op2
        except:
            raise ZeroDivisionError("division by zero") 


def rpn_calc(filename: str) -> int:
    # TODO: Read lines from the file and pass them to the postfix_eval
    
    with open(filename, "r") as r:
        for expr in r:
            postfix_expr = postfix_eval(expr.strip().split())
    

