my_List = []
while(True):
        inp = input("Enter a number")
        if inp == 'done': break
        value = float(inp)
        my_List.append(value)

print(sum(my_List)/len(my_List))
