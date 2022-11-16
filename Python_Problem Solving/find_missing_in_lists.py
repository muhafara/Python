'''Find the missing elemen in a list'''
'''Tip: n-series equation
n = n * (n+1) / 2
'''
myList =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30]

def find_missing(list,n):
    sum1 = 30  * 31 / 2
    sum2 = sum(list)

    print(sum1)
    print(sum2)
    print(sum1-sum2)

find_missing(myList,30)
