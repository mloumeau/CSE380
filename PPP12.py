from math import ceil as c

def calcInitials(n):
    # YOUR CODE GOES HERE
    return n**2 * (n+1) * 2**6

def hole_pigeon(p):
    # YOUR CODE GOES HERE
    return c(p/calcInitials(26))

population = 1826160
print(hole_pigeon(population))
# print(c(1826160/(26**2*27*2**6)))