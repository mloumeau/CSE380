from math import ceil, log
from collections import Counter
import sympy

def buildTree(counterList):
    if len(counterList) < 2:
        return counterList[0][0]
    tempList = counterList
    temp1 = tempList.pop()
    temp2 = tempList.pop()
    temp3 = ((temp1[0], temp2[0]), temp1[1] + temp2[1])
    tempList.append(temp3)
    newCounter = Counter(dict(tempList))
    return(buildTree(newCounter.most_common()))


def readTree(treeList, sizeStr):
    if type(treeList) != tuple:
        return [(treeList, sizeStr)]
    newList = []
    if type(treeList[0]) == tuple:
        newList += readTree(treeList[0], sizeStr + 1)
    else:
            newList.append((treeList[0], sizeStr))
    if type(treeList[1]) == tuple:
        newList += readTree(treeList[1], sizeStr + 1)
    else:
        newList.append((treeList[1], sizeStr))
    return newList


def findCompressionRatio(list_of_gaps, asciiSize):
    list_of_frequencies = []
    list_of_unique_gaps = []
    numBitsDict = {}
    total_bits = 0
    
    counterForList = Counter(list_of_gaps)
    tempCounterList = counterForList.most_common()
    
    # Get list of frequencies
    for x in tempCounterList:
        list_of_frequencies.append(x[1])
        list_of_unique_gaps.append(x[0])
        numBitsDict[x[0]] = 0
    
    for x in readTree(buildTree(tempCounterList), 1):
        numBitsDict[x[0]] = x[1]

    for x in range(0, len(list_of_unique_gaps)):
        total_bits += list_of_frequencies[x] * numBitsDict.get(list_of_unique_gaps[x])
    total_characters = len(list_of_gaps)
    total_unique_characters = len(list_of_unique_gaps)
    fixed_bits_per_character = ceil(log(total_unique_characters, 2))
    total_fixed_bits = total_characters * fixed_bits_per_character
    if total_fixed_bits == 0:
        return 0
    compression_ratio = (total_fixed_bits - total_bits) / total_fixed_bits
    print("From Fixed:  ", compression_ratio * 100, "%")
    print("From Binary: ", (((9999998 * 32) - total_bits) / (9999998 * 32)) * 100, "%")
    print("From ASCII:  ", (asciiSize - total_bits) / asciiSize *100, "%")
    return compression_ratio

def asciiCompression():
    list_of_gaps = []
    prev = 3
    gap = 0
    sizeASCII = 0
    
    for primeVal in list(sympy.primerange(sympy.prime(3), sympy.prime(10000000))):
        gap = primeVal - prev
        prev = primeVal
        list_of_gaps.append(gap)
        # Each char is one byte (8 bits).
        # Then we add one extra char indicating a new line (\n or other new line char)
        sizeASCII += (len(str(primeVal)) + 1) * 8

    findCompressionRatio(list_of_gaps, sizeASCII)
    
asciiCompression()

def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]