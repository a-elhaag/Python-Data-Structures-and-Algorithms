def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(my_list, start_index, end_index):
    if start_index < end_index:
        pivot_index = pivot(my_list, start_index, end_index)
        quick_sort_helper(my_list, start_index, pivot_index - 1)
        quick_sort_helper(my_list, pivot_index + 1, end_index)




