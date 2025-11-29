def merge_lists(list1, list2, reverse=False):
    merged = []
    i,j = 0,0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    while i < len(list1):
        merged.append(list1[i])
        i += 1
    while j < len(list2):
        merged.append(list2[j])
        j += 1
    if reverse:
        reversed_list = []
        for k in range(len(merged) - 1, -1, -1):
            reversed_list.append(merged[k])
        return reversed_list

    return merged

list1 = [1, 3, 10]
list2 = [0, 4, 7, 9]

print(merge_lists(list1, list2))
print(merge_lists(list1, list2, True))