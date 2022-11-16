'''
def fibonacci(n):
    my_List = [0,1]
    first_num = 0 
    second_num = 1
    for i in range(2,n):
        fibnocci = first_num + second_num
        first_num, second_num = second_num, fibnocci
        my_List.append(fibnocci)
    return my_List
'''
def fibonacci(n):
    count,n1 = 0,0
    n2 =1
    ans = []
    
    while count < n:
        ans.append(n1)
        nth = n1 + n2
        # update the new values 
        n1, n2 = n2, nth
        count += 1
    return ans

#fibnocci_List = list(map(fibnocci_number,))
cube = lambda x: x**3
print(cube(3))

print(list(map(cube, fibonacci(1))))
''''
0 1 2 3 4 5 6 7
0 1 1 2 3 5 8 13
'''        

