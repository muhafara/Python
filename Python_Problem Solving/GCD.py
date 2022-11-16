import math
'''Find GCD (GRETOR COMMON DIVISOR)'''

'''GCD USING RECURSIVE FUNCTION'''

'''Eucalidean Algorithm'''
'''gcd(a,b) = if (a,0) = a'''
'''gcd(a,b) = (b, a mod b)'''

def gcd_Recursive(a, b):
    assert int(a) == a and int(b) == b
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd_Recursive(b , a % b)

#print(gcd_Recursive(36,48))

'''Gcd using math.gcd function'''
def math_GCD_Function(num_1, num_2):
    return math.gcd(num_1, num_2)

print(math_GCD_Function(24,36))
    

