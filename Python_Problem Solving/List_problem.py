'''Given an array of integer return indicies of twoo number suchthey add upto given number

nums[2,7,11,15] gien number = 9 --> output = [2,7]'''

nums = [2,7,11,15]

def return_Numbs(list, num):
    for i in list:
        if list[i] + list[i+1] == num:
            print(f"first num is {i} and second num is {i+1}")
            break
        else:
            print("Not found")

print(return_Numbs(nums,9))