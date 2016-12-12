#import a function for calculating square root from the math module as "sr" for brevity's sake 
from math import sqrt as sr
#import sympy to work with symbols.
import sympy

def is_py(*args):
	a,b,c = sorted(args)
	return a ** 2 + b**2  == c**2
def find_hyp(a,b):
    return sr(a ** 2 + b ** 2)
def find_leg(*args):
    return sr(max(args) ** 2 - min(args) ** 2)
def consecutive(length, total, inc,pos):
        total = total - sum([i for i in list(range(inc,length * inc,inc))])
        first = total / length
        result = first + (pos - 1) * inc
        return result
def vol_sphere(r):
        a = (4/3) * (r ** 3)
        b = round((4/3) * (r ** 3) * 3.14,2)
        return """In pi: {0} times pi.In terms of 3.14: {1}""".format(a,b)
def vol_cone(r,h):
        a = (r ** 2) * (h / 3)
        b = round((r ** 2) * (h / 3) * 3.14,2)
        return """In pi: {0} times pi.In terms of 3.14: {1}""".format(a,b)
def vol_cyl(r,h):
        a = r ** 2 * h
        b = round(r ** 2 * h * 3.14,2)
        return """In pi: {0} times pi.In terms of 3.14: {1}""".format(a,b)
solve_unknown = sympy.solveset

