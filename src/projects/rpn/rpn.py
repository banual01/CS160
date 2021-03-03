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
    eval_stack = postfix_expr.spilt()
    math_stack = Stack()
    for str_index in range(len(eval_stack)):
        if eval_stack[str_index] not in {"+", "-", "*", "/"}:
            try:
                int(eval_stack[str_index])
                float(eval_stack[str_index])
                operation = int(eval_stack[str_index])
                math_stack.push(operation)
            except:
                raise TokenError(f"Unknown token: {eval_stack[str_index]}")
        else: 
            try:
                op2 = math_stack.pop()
                op1 = math_stack.pop()
                math_stack.push(do_math(eval_stack[str_index], op1, op2))
            except:
                raise StackError("Stack is empty")    
    if math_stack.size() > 1:
        raise StackError("Stack is not empty")
    return math_stack.peek()




def do_math(op: str, op1: int, op2: int) -> int:
    # TODO: Process arithmetic operations
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2


def rpn_calc(filename: str) -> int:
    # TODO: Read lines from the file and pass them to the postfix_eval
    
    with open(filename, "r") as r:
        expr = r.readline()
        postfix_expr = postfix_eval(expr)
    

