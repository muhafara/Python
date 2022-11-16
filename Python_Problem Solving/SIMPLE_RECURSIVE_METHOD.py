#Recursive method to print number from 0 to 5
def print_Recursive_Method(n):
    if n == 0:
        print(n)
    else:
         print_Recursive_Method(n-1);
         print(n)

print_Recursive_Method(5)
