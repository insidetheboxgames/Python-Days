#day 14 - 30 Day challenge: Python Type Errors

# Types of Errors
# Syntax Error: forgetting to enclose with parenthesis
# EX: print 'Hello World'
# Fix: print('Hello World')
# Name Error: variable that is trying to be assigned without being defined.
# EX: print(age) and age has never been defined
# Fix: age = 19 print(age)
# Index Error: When you go out of range of a list or string
# EX: numbers = [1,2,3,4,5] numbers[5] the max index is [4]
# ModuleNotFound Error: module does not exist
# EX import maths
# Fix: import math
# Attribute Error: calling something from a module that does not exist
# EX: import math math.PI
# FIX: import math math.pi
# Key Error: There is a typo in the key for a dictionary
# Fix: Fix the typo
# Import Error: trying to import something that does not exist
# EX: from math import power
# Fix: from math import pow
# Value Error: Cannot change a type into another type because of different types
# EX: int('12a')
# Fix: int(12)
# Zero Division Error: Can not divide by zero
# Fix: Just don't divide by zero