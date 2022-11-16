def unique_names(names1, names2):
    get_List = names1 + names2
    unique_List = []
    for i in get_List:
        if i not in unique_List:
            unique_List.append(i)
    return unique_List

if __name__ == "__main__":
    names1 = ["Ava", "Emma", "Olivia"]
    names2 = ["Olivia", "Sophia", "Emma"]
    print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia