# Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.
# Return the two integers in any order.

def closestDivisors(num):
    """
    :type num: int
    :rtype: List[int]
    """
    result, d = [1, num+1], 1
    while d**2 <= num + 2:
        if (num+2) % d == 0:
            result = [d, (num+2)//d]
        if (num+1) % d == 0:
            result = [d, (num+1)//d]
        d+=1
    return result

t1 = closestDivisors(123) # Expected: [5, 25]
print(t1)
t2 = closestDivisors(999) # Expected: [25, 40]
print(t2)