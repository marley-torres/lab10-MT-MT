"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a, b):
    try:
        val = math.log(b, a)
        return val
    except Exception:
        raise ValueError

def exponent(a, b):
    return a ** b


def sub(a,b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    try:
        value = math.log(b, a)
        return value
    except Exception:
        raise ValueError

def exp(a, b):
    return a ** b


