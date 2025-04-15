"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    try:
        val = math.hypot(a, b)
        return val
    except Exception as e:
        raise Exception(str(e))

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a,b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    try:
        val = math.log(b, a)
        return val
    except Exception:
        raise ValueError 

def exponent(a, b):
    return a ** b



