# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # `07.ipynb`

# ## ❄ Problem 1 ❄
#
# [🍅 Classes: Dealing with Complex Numbers | HackerRank](https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem)
#
# ---
#
# <center>
# <img src=images/1-instructions.png style="width: 75%">
# </center>

# +
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, no):
        c = Complex(0, 0)
        c.real = self.real + no.real
        c.imaginary = self.imaginary + no.imaginary
        return c
    
    def __sub__(self, no):
        c = Complex(0, 0)
        c.real = self.real - no.real
        c.imaginary = self.imaginary - no.imaginary
        return c
        
    def __mul__(self, no):
        c = Complex(0, 0)
        c.real = (self.real * no.real) - (self.imaginary * no.imaginary)
        c.imaginary = (self.real * no.imaginary) + (self.imaginary * no.real)
        return c

    def __truediv__(self, no):
        c = Complex(0, 0)
        a = (self.real * no.real) + (self.imaginary * no.imaginary)
        c.real = a / (no.real ** 2 + no.imaginary ** 2)
        b = (self.imaginary * no.real) - (self.real * no.imaginary)
        c.imaginary = b / (no.real ** 2 + no.imaginary ** 2)
        return c

    def mod(self):
        c = Complex(0,0)
        c.real = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return c

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
# -


# ## HackerRank screenshot for problem 1
#
# <center>
# <img src=images/1.png style="width: 75%;">
# </center>
