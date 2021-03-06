''' PROJECT EULER: PROBLEM 25: 1000-DIGIT FIBONACCI NUMBER

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

'''
from math import sqrt
from decimal import Decimal, localcontext


def fib(n):
    with localcontext() as ctx:
        ctx.prec = 1000
        # Calculate Fib for n term
        Phi = ((Decimal(1) + Decimal(sqrt(5)))/Decimal(2)) ** Decimal(n) # GOLDEN RATIO
        Psi = ((Decimal(1) - Decimal(sqrt(5)))/Decimal(2)) ** Decimal(n) # GOLDEN RATIO

        F_n = (Phi - Psi) / Decimal(sqrt(5))
    return int(F_n)

n_cycle = 1
n = 1

while len(str(n_cycle)) < 1000:
    # Cycle until we find the first term that is 4 digits.
    # This will break the above condition and we will exit.
    n += 1
    n_cycle = fib(n)

print(n)
















# end.
