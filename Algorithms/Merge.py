def merge(list_1, list_2):
    combined = []
    i = j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            combined.append(list_1[i])
            i += 1
        else:
            combined.append(list_2[j])
            j += 1
    combined += list_1[i:]
    combined += list_2[j:]
    return combined


def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list

    mid_index = len(my_list) // 2
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)


# Recursively call the merge_sort function on the left and right halves of the list, created by slicing my_list using mid_index. Store the sorted left half in the variable left and the sorted right half in the variable right.

# Call the previously implemented merge function to combine the sorted left and right halves into a single sorted list.

# Return the sorted list.
