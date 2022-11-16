'''Write a program which return product of a list'''

my_list = [3,2,3]

def productof(mylist):
    product = 1
    for i in mylist:
        product = i * product
    return product

print(productof(my_list))