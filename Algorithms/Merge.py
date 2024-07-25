class Merge:
    @staticmethod
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

    @staticmethod
    def merge_sort(my_list):
        if len(my_list) <= 1:
            return my_list

        mid_index = len(my_list) // 2
        left = Merge.merge_sort(my_list[:mid_index])
        right = Merge.merge_sort(my_list[mid_index:])

        return Merge.merge(left, right)


