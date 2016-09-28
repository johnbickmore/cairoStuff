from math import sqrt, trunc
import numpy as np
import IPython

class Quadratic(object):

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self,x):
        if x is None:
            return None
        result = (self.a * pow(x,2)) + (self.b * x) + self.c
        return -result

    def intersect(self,q2):
        aprime = q2.a - self.a
        bprime = q2.b - self.b
        cprime = q2.c - self.c
        
        q3 = Quadratic(aprime,bprime,cprime)
        
        xs = q3.solve()
        xs_existing = np.array([x for x in xs if x is not None])
        return xs_existing

    def discriminant(self):
        return pow(self.b,2) - (4 * self.a * self.c)

    def solve(self):
        D = self.discriminant()
        numerator_a = -self.b
        denominator = 2 * self.a
        if D < 0:
            return [None,None]
        elif D == 0 or self.a == 0:
            print('Only one intersection')
            #using mullers method:
            twoc = - 2 * self.c
            sqrtb4ac = sqrt(pow(self.b,2) - (4 * self.a * self.c))
            pos = self.b + sqrtb4ac
            neg = self.b - sqrtb4ac
            if pos != 0:
                x = twoc / pos
            else:
                x = twoc / neg
            return [x,None]
        else:
            z = sqrt(D)
            return [
                (numerator_a + z) / denominator,
                (numerator_a - z) / denominator,
            ]
        