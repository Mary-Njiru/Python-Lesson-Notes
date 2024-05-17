def add(x,y):
    result = x+y
    return result

def substract(x,y):
    result = x-y
    return result

def divide(x,y):
    result = x/y
    return result

def multiply(x,y):
    result = x*y
    return result

def remainder(x,y):
    result = x%y
    return result

def power_of(x):
    result = x**3
    return result

# Positional Arguments

def sum(*numbers):
    total = 0
    for number in numbers:
        total+=number
    return total

def multiply_many(*myList):
    result = 1
    for x in myList:
        result = result * x
    return result



