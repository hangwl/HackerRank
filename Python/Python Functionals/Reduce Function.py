
# a lambda function is a small anonymous function.
# it can take any number of arguments, but can only have one expression

# for example:

"""def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2) # n is assigned as 2

print(mydoubler(11)) # takes argument a = 11 and returns expression 11 * 2"""

from fractions import Fraction
# The fractions module provides support for rational number arithmetic.
# class fractions.Fraction(numerator=0, denominator=1)

from functools import reduce
# The reduce() function applies a function of two arguments cumulatively on a list of objects in succession from left to right to reduce it to one value. 
# Say you have a list, say [1,2,3] and you have to find its sum.

def product(fracs):
    t = Fraction(reduce(lambda x, y: x*y, fracs))
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)