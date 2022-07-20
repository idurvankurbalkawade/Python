import math
def add(*x):
    return sum(x)

def sub(*x):
    result=x[0]
    for i in x[1:]:
        result=result-i
    return result

def multiply(*x):
    return math.prod(x)

def divide(x,y):
    return x/y
