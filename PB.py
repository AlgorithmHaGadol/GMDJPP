#import a function for calculating square root from the math module as "sr" for brevity's sake 
from math import sqrt as sr

#import sympy to work with symbols.
import sympy

#function for checking whether or not set of points makes a right triangle.
#takes the measurement of each of the three sides as arguments
def is_py(l1,l2,h):
	return l1 ** 2 + l2 ** 2  == h**2

#function for finding the hypotenuse of a right triangle
#takes the measurement of each of its legs as arguments
def find_hyp(l,h):
    return sr(l ** 2 + h ** 2)

#function for finding the hypotenuse of a right triangle
#takes the measurement of one leg and the hypotenuse as arguments
def find_leg(*args):
    return sr(max(args) ** 2 - min(args) ** 2)

#function for
def consecutive(length, total, inc):
        """total = total - sum([i for i in list(range(inc,length * inc,inc))])
        first = total / length
        result = first + (pos - 1) * inc
        return result"""
        units_to_add
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

