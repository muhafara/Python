'''Find the sum of the digits of a positive number'''

def sumOfDigits(number): 
    sum = 0
    for var in str(number):
        sum += int(var)
    return sum

print(sumOfDigits(51))

'''Find sum of digits using recursive method'''

'''recursive case is (n%10) + (n//10)'''

def sumOfDigitsRecursive(number):
    assert number >= 0 and int(number) == number, 'Please enter the positve integer'
    if number == 0:
        return 0
    else:
        return int(number % 10) + sumOfDigitsRecursive(int(number//10))


print(sumOfDigitsRecursive(435))