from array import *

my_arr = array('i',[1,2,3,4,5])

'''inserting an element at the end of array'''
#my_arr.insert(5,5)

'''inserting an element at the begining'''
#my_arr.insert(0,1)

'''inserting element using append method
append () can add element at the end of the array only
'''
#my_arr.append(7)

'''Acessing element of an array using index'''

'''Traversal of an array'''
def array_Traversal():
    for i in my_arr:
        print(i)

#array_Traversal();

'''Accesing element in an array'''
def accessing_Element(array, index):
    if index >= len(array):
        print("Number must be lower")
    else:
        print(array[index])


#accessing_Element(my_arr,5)

'''Searching a given value in array'''

def search_Value(array, search):
    for i in array:
        if i == search:
            return array.index(search)
    return "The element does't found"

#print(search_Value(my_arr,7))

'''Deleting an element from an array'''
delete_Array = array ('i',[23,12,34,54])
#print(delete_Array)
delete_Array.remove(34)
#print(delete_Array)

'''Extending Array'''
arr_1 = array('i', [23,54])

arr_2 = array('  i', [57,64])

arr_1.extend(arr_2)
print(arr_1)

