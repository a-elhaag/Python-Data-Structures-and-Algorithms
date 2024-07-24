class Basic_sorts:
    @staticmethod
    def bubble_sort(arr):
        if not arr:
            return []
        for i in range(len(arr)):
            for j in range(len(arr) - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = (
                        arr[j + 1],
                        arr[j],
                    )
        return arr

    def selection_sort(arr):
        if not arr:
            return []
        for i in range(len(arr)):
            min_item = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_item]:
                    min_item = j
            if min_item != i:
                arr[i], arr[min_item] = arr[min_item], arr[i]
        return arr

    def insertion_sort(arr):
        if arr is None:
            return []
        for i in range(1, len(arr)):
            temp = arr[i]
            j = i - 1
            while temp < arr[j] and j >= 0:
                arr[j + 1] = arr[j]
                arr[j] = temp
                j -= 1
        return arr


