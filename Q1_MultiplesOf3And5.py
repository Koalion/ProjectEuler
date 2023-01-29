# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def sumOfMultiplesOf3And5 (limit) :
    """function returns the sum of all the multiple of 3 and 5 under the limit value"""
    an3 = limit - 1
    an5 = limit - 1
    an15 = limit - 1

    while an3 % 3 != 0 :
        an3 = an3 - 1

    while an5 % 5 != 0 :
        an5 = an5 - 1
    
    while limit >= 15 and an15 % 15 != 0 :
        an15 = an15 - 1
    
    n3 = an3 / 3
    n5 = an5 / 5
    n15 = an15 / 15

    if limit >= 15 : sum = int(n3 / 2 * (3 + an3) + n5 / 2 * (5 + an5) - n15 / 2 * (15 + an15))
    else : sum = int(n3 / 2 * (3 + an3) + n5 / 2 * (5 + an5))

    return sum

print(sumOfMultiplesOf3And5(1000))
print(sumOfMultiplesOf3And5(1000000000000))