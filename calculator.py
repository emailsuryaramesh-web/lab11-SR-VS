#https://github.com/emailsuryaramesh-web/lab11-SR-VS.git
#Surya Ramesh
#Vennela Sadineni
import math
# First example
def add(a, b): 
    return a + b
def hypotenuse(a, b):
    return math.hypot(a, b)

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b
def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)
def logarithm(a, b):
    if a<= 0 or b<=0:
        raise ValueError
    return math.log(b, a)


def exp(a, b):
    return a ** b

