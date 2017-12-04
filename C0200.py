import math

def Fibonatti(r):
    a , b , c = 0, 1, 1
    while(0 < r):
        yield c
        a = b
        b = c
        c = a + b

y = [int((((1 + 5**0.5)/2)**c-((1 - 5**0.5)/2)**c)/5**0.5) for c in range(10)]

