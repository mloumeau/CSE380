import sympy
from math import *


# Extra Helper functions:

# Computes least common multiple.
# Taken from https://stackoverflow.com/questions/51716916/built-in-module-to-calculate-least-common-multiple
# Also, aparently there is a lcm() in Python 3.9, but I'm not using Python 3.9.
def lcm(a, b):
    return abs(a*b) // gcd(a, b)




# Hash generaton:

# Maps a single element to a prime
def mapElmToPrime(elm):
    return sympy.prime(elm)

# Maps set elements to prime numbers.
def encodeSet (nSet):
    newset = list()
    for x in nSet:
        newset.append(sympy.prime(x))
    return newset

# Computes hash based on prime number mapping.
def hashEncodingSet (nSet):
    hash = 1
    for x in nSet:
        hash *= x
    return hash

# Gets Godel Hash for a set.
def hashSet(nSet):
    return hashEncodingSet(encodeSet(nSet))




# Hash set functions:

# Tests set membership. If element is a member or subset of the.
# hash, it returns True. Else, it returns False.
def hashIsMember(hash, member):
    if ((hash % member) == 0):
        return True
    else:
        return False

# Returns the union of two hashed sets as a hash.
def hashUnion(hash1, hash2):
    return lcm(hash1, hash2)

# Returns intersection of two hashed sets as a hash.
def hashIntersect(hash1, hash2):
    return gcd(hash1, hash2)

# Adds an element to the set if not already included.
def hashAddElm (hash, addElm):
    # Ensuring the element is prime guards against problematic subsets.
    # For exaple, if hash represents {2 4 5} and addElm represents {2 3}
    # this code could block it rather than multiplying {2}'s prime
    # representation to hash a second time.
    if ((not hashIsMember(hash, addElm)) and sympy.isprime(addElm)):
        return hash * addElm
    else:
        return hash

# Removes an element from the set if included.
# Unlike hashAddElm, rmvElm can be a subset.
def hashRmvElm(hash, rmvElm):
    if (hashIsMember(hash, rmvElm)):
        return hash / rmvElm
    else:
        return hash

# Gets the compliment of hash1 by hash2.
def hashCompliment(hash1, hash2):
    return hash1 / gcd(hash1, hash2)




# Godel hashes in poset
# According to a post on the DM2 discussion board by Jacob Barnes,
# we needed to code some way to show that relations can be encoded as
# sets of pairs. This is my attempt to fulfill that requirement.
def encodeHashRelation():
    relation = list()
    baseSet = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    for x in baseSet:
        for y in baseSet:
            if (hashIsMember(hashSet(y), hashSet(x))):
                relation.append((hashSet(x), hashSet(y)))
    return relation




# Tests:
print("Test 0, relations as sets of pairs:")
print(encodeHashRelation())


if (hashSet((1, 3, 4)) == hashSet((1, 3, 4))):
    print("Test 1 Passed")
else:
    print("Test 1 Failed")


if (hashIsMember(hashSet((1, 3, 4)), mapElmToPrime(3)) == True):
    print("Test 2 Passed")
else:
    print("Test 2 Failed")


if (hashIsMember(hashSet((14, 3, 4, 6, 7)), mapElmToPrime(9)) == False):
    print("Test 3 Passed")
else:
    print("Test 3 Failed")


if (hashIsMember(hashSet((1, 3, 4)), hashSet((1, 3))) == True):
    print("Test 4 Passed")
else:
    print("Test 4 Failed")


if (hashUnion(hashSet((19, 45, 6)), hashSet((5, 2, 3))) == hashSet((2, 3, 5, 6, 19, 45))):
    print("Test 5 Passed")
else:
    print("Test 5 Failed")


if (hashUnion(hashSet((19, 45, 6)), hashSet((6, 19))) == hashSet((6, 19, 45))):
    print("Test 6 Passed")
else:
    print("Test 6 Failed")


if (hashUnion(hashSet((19, 45, 6)), mapElmToPrime(7)) == hashSet((6, 19, 7, 45))):
    print("Test 7 Passed")
else:
    print("Test 7 Failed")


if (hashIntersect(hashSet((3, 4, 5, 2, 7, 1, 8)), hashSet((4, 5, 10, 7))) == hashSet((4, 5, 7))):
    print("Test 8 Passed")
else:
    print("Test 8 Failed")


if (hashIntersect(hashSet((4, 8, 15, 21)), hashSet((4, 8, 21, 15))) == hashSet((4, 15, 8, 21))):
    print("Test 9 Passed")
else:
    print("Test 9 Failed")


if (hashIntersect(hashSet((4, 8, 15)), mapElmToPrime(6)) == 1):
    print("Test 10 Passed")
else:
    print("Test 10 Failed")


if (hashAddElm(hashSet((1, 3, 5)), mapElmToPrime(3)) == hashSet((1, 3, 5))):
    print("Test 11 Passed")
else:
    print("Test 11 Failed")


if (hashAddElm(hashSet((1, 3, 5)), mapElmToPrime(4)) == hashSet((1, 3, 4, 5))):
    print("Test 12 Passed")
else:
    print("Test 12 Failed")


# hashAddElm cannot add two sets together. Use union.
if (hashAddElm(hashSet((1, 3, 5)), hashSet((3, 4))) == hashSet((1, 3, 5))):
    print("Test 13 Passed")
else:
    print("Test 13 Failed")


if (hashRmvElm(hashSet((4, 6, 2)), mapElmToPrime(5)) == hashSet((4, 2, 6))):
    print("Test 14 Passed")
else:
    print("Test 14 Failed")


if (hashRmvElm(hashSet((4, 6, 2)), mapElmToPrime(2)) == hashSet((4, 6))):
    print("Test 15 Passed")
else:
    print("Test 15 Failed")


# hashRmvElm can remove a subset of the set without issue.
if (hashRmvElm(hashSet((4, 6, 2)), hashSet((6, 2))) == mapElmToPrime(4)):
    print("Test 16 Passed")
else:
    print("Test 16 Failed")


if (hashCompliment(hashSet((6, 7, 3)), hashSet((5, 4, 19))) == hashSet((7, 6, 3))):
    print("Test 17 Passed")
else:
    print("Test 17 Failed")


if (hashCompliment(hashSet((6, 7, 3)), hashSet((5, 3, 19))) == hashSet((7, 6))):
    print("Test 18 Passed")
else:
    print("Test 18 Failed")


if (hashCompliment(hashSet((6, 7, 3)), hashSet((6, 7, 3))) == 1):
    print("Test 19 Passed")
else:
    print("Test 19 Failed")