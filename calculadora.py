#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Calculator with +, -, *, / operators
"""

import sys

if (len(sys.argv) != 4):
    sys.exit("\nUsage error: calculadora.py Function Operand1 Operand2\n")

function = sys.argv[1]
try:
    operand1 = float(sys.argv[2])
    operand2 = float(sys.argv[3])
except ValueError:
    sys.exit("\nError: One of the values entered is not a number\n")

if (function == "mult"):
    result = operand1 * operand2
    operator = "*"
elif (function == "add"):
    result = operand1 + operand2
    operator = "+"
elif (function == "sub"):
    result = operand1 - operand2
    operator = "-"
elif (function == "div"):
    result = operand1 / operand2
    operator = "/"
else:
    sys.exit("\nError: Function entered is not available\n")

print str(operand1), operator, str(operand2), "=", str(result)
