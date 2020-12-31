# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 19:20:43 2020

@author: matth
"""
import sympy
from math import gcd

# for x in range(1,151):
#     print((pow(x, 341) - x) % 341) 
        
# def findCoprimes(n):
#     coprimeList = []
#     for x in range(1,101):
#         if gcd(x,n) == 1:
#             coprimeList.append(x)
#     return coprimeList


# for n in range (1000, 10000):
#     for x in findCoprimes(n):
#         if ((x**n) - x) % n == 0:
#             print(n)
#             break
        
def factorization(num):
    all_factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            all_factors.append(i)
    return all_factors

def check_prime_largest(num):
    largest = num[0]
    for x in num:
        if sympy.isprime(x):
            if largest < x:
                largest = x
                
    return largest

CEP = (sympy.prime(1224))
NYEP = (sympy.prime(1231))

largestPrimeC = check_prime_largest(factorization(CEP - 1))
largestPrimeN = check_prime_largest(factorization(NYEP - 1))

print("Test 1 (Christmas Eve Prime)")
print("Largest Prime Factor of p - 1:", largestPrimeC)
print("Largest Prime Factor of Largest Prime Factor of (p - 1):", check_prime_largest(factorization(largestPrimeC - 1)))
print("Largest Prime Factor of p + 1:", check_prime_largest(factorization(CEP + 1)))

print("\nTest 2 (New Year's Eve Prime)")
print("Largest Prime Factor of q - 1:",largestPrimeN)
print("Largest Prime Factor of Largest Prime Factor of (q - 1):",check_prime_largest(factorization(largestPrimeN - 1)))
print("Largest Prime Factor of q + 1:",check_prime_largest(factorization(NYEP + 1)))

#print(factorization(9929 - 1))

