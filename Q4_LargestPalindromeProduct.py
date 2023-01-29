# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def findLargestPalindrome(num) :
    """Function returns the biggest palindrome number that can be achieved as a product of two num-digit numbers"""
    x = []
    for a in range(10**num-1,0, -1) :
        for b in range(10**num-1, a-1, -1):
            if str(a*b) == str(a*b)[::-1] : x.append(a*b)
    return max(x)

print(findLargestPalindrome(3))
