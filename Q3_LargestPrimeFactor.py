# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

def findLargestPrimeFactor(num) :
    """function finds a largest prime factor of a given number, returns integer"""

    maxPrime = 1

    while num % 2 == 0 :
        maxPrime = 2
        num /= 2
    
    for ind in range(3, int(math.sqrt(num)), 2) :
        while num % ind == 0 :
            maxPrime =  ind
            num /= ind
        
    if num > 2 :
        maxPrime = num
    
    return maxPrime

print(findLargestPrimeFactor(600851475143))
