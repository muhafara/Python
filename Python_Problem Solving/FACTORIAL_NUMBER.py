import math
#FUNCTION TO FIND A FACTORICAL OF A NUMBER

# FACTORIAL = N = N * N -1
# FACTORIAL OF 4: 4*3*2*1 =24

#USING for LOOP

def find_FactorialF(number):
    assert number >= 0 and int(number) == number, 'Number must be a positive Integer only'
    for var in range(1,number):
       number *= var
    return number

# using while loop 
def find_FactorialW(number):
    assert number >=0 and int(number) == number, 'Number must be a positive integer'
    i = number - 1
    while i > 0:
        number *= i
        i -= 1
    return number 

#using recursive function

def find_FactorialR(number):
    assert number >=0 and int(number), 'Number should be a positive integer'
    if number in [0,1]:
        return 1
    else:
        return number * find_FactorialF(number-1)

'''using factorial method from math'''
def factorial_using_math(number):
    return math.factorial(number)
    


'''Calling function using recursive function to find factorial'''
print(find_FactorialR(6))
'''Calling function using for loop to find factorial'''
print(find_FactorialF(5))
'''Calling function using while loop to find factorial'''
print(find_FactorialW(4))
'''Calling math.factorial'''
print(factorial_using_math(4))