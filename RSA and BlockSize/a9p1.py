#!/usr/bin/env python3

# ---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2020 <<Junyao Cui>>
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
# ---------------------------------------------------------------

"""
Assignment 9 Problem 1
"""

from sys import flags
from typing import Tuple


def finitePrimeHack(t: int, n: int, e: int) -> Tuple[int, int, int]:
    """
    Hack RSA assuming there are no primes larger than t
    """
    factors = getPrimeFactor(n)
    if len(factors) != 2:
        print("The number n should only have two prime factors.")
        exit()
    #print(factors)    
    if factors[0] <= t:
        p = factors[0]
    else:
        print("All prime factors should be no larger than t")
        exit()
        
    if factors[1] <= t:
        q = factors[1]
    else:
        print("All prime factors should be no larger than t")
        exit()
    
    modul = (p - 1) * (q - 1)
    
    d = modInv(e, modul)
    
    return [p, q, d]

def euclidean_gcd(a, m):
    # ax + my = g = gcd(a,m)
    # by using Euclidean algorithm
    # when a = 0: simply (ax + my = gcd(a, m)), holds when x = 0, y = 1, since gcd(0, m) = m
    # Otherwise,  (a mod m)x' + ay'= gcd(a,m)
    if a == 0:
        return (m, 0, 1)
    else:
        g, y, x = euclidean_gcd(m % a, a)
        return (g, x - (m // a) * y, y)
    

def modInv(a, m):
    # before doing the modular inverse, the gcd(a, m) should be 1 
    # check the gcd(a, m)
    g, x, y = euclidean_gcd(a, m)
    if g != 1:
        return None
    else:
        return x % m    
     

def getPrimeFactor(n):
    i = 2
    factors = []
    while i <= n:
        if (n % i) == 0:
            factors.append(i)
            n = n / i
        else:
            i = i + 1
    return factors
            
            
    
def test():
    "Run tests"
    assert finitePrimeHack(100, 493, 5) == [17, 29, 269]
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking
    print(finitePrimeHack(2**14,8989,69))
    print(finitePrimeHack(2**14,11639,127))
    print(finitePrimeHack(2**14,7739,79))
    print(finitePrimeHack(2**14,8137,79))
    print(finitePrimeHack(2**14,4757,103))

# Invoke test() if called via `python3 a5p1.py`
# but not if `python3 -i a5p1.py` or `from a5p1 import *`
if __name__ == '__main__' and not flags.interactive:
    test()
