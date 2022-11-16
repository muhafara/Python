'''
Find the runner score in the list
Given Array = [2,3,6,6,5]
should return 5
'''
from array import *
myArray =array('i',[57,57,-57,57])
runner_up = list(sorted(set(myArray)))
print(runner_up[-2])

