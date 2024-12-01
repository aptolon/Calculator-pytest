import math
def add(x, y):
    if type(x) != (int or float) or type(y) != (int or float):
        raise TypeError("x и y должны быть числами")
    return x + y

def subtract(x, y):
    if type(x) != (int or float) or type(y) != (int or float):
        raise TypeError("x и y должны быть числами")
    return x - y

def multiply(x, y):
    if type(x) != (int or float) or type(y) != (int or float):
        raise TypeError("x и y должны быть числами")
    return x * y

def divide(x, y):
    if type(x) != (int or float) or type(y) != (int or float):
        raise TypeError("x и y должны быть числами")
    if y == 0:
        raise ZeroDivisionError("деление на ноль")
    return x / y

def percentage(x, y):
    if type(x) != (int or float) or type(y) != (int or float):
        raise TypeError("x и y должны быть числами")
    return (x/100) * y

def power(x, y):
    if type(x) != (int or float) or type(y) != (int or float):
        raise TypeError("x и y должны быть числами")
    return x ** y

def log(x):
    if type(x) != (int or float):
        raise TypeError("x должен быть числом")
    if x <= 0:
        raise ValueError("x должен быть больше 0")
    return math.log(x)

def factorial(x):
    if type(x) != int:
        raise TypeError("x должен быть целым числом")
    if x < 0:
        raise ValueError("x не может быть отрицательным")
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)


