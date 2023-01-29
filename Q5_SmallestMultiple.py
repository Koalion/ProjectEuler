# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def findLcmOfRange(start, end) :
    """function returns least common multiplier of number in a given range of natural numbers (inclusive), return int"""
    numbersTab = range(start, end + 1)

    if start == 1 : factor = start + 1
    else : factor = start
    lcm = 1

    while factor <= end :

        wasDivided = False

        if sum(numbersTab) == end + 1 - start :
            break

        for val in numbersTab :
            if val % factor == 0 :
                numbersTab = [ i / factor if i % factor == 0 else i for i in numbersTab ]
                lcm *= factor
                wasDivided = True
                break

        if wasDivided == False :
            factor += 1

    return lcm
        
print(findLcmOfRange(2,20))