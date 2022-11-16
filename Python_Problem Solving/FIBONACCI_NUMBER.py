#Fibonacci series is 0 , 1, 1, 2, 3, 5, 8, 13, 21, 34 ...........n

#using recurcive function to get fibonacci value 
# f(n) = f(n-1) + f(n-2)

import numbers


def fibonacci_Number(number):
    assert number >= 0 and int(number) == number, 'Fibanocci number needs to be greater than 0'
    if number in [0,1]:
        return number
    else:
        return fibonacci_Number(number-1) + fibonacci_Number(number-2)

# Calling fibonacci function
#print(fibonacci_Number(7))

'''List of fibonacci number using loop'''
def fibonacci_Number_Using_Loop(number):
    print("0\n1")
    previous , next = 0 , 1
    for var in range(1,number):
        fibnocci_number = previous + next
        previous = next
        next = fibnocci_number
        print(fibnocci_number)

fibonacci_Number_Using_Loop(8)