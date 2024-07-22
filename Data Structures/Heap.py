class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _sink_down(self, index):
        max_index = index
        left_child = self._left_child(index)
        right_child = self._right_child(index)
        if left_child < len(self.heap) and self.heap[left_child] > self.heap[max_index]:
            max_index = left_child
        if (
            right_child < len(self.heap)
            and self.heap[right_child] > self.heap[max_index]
        ):
            max_index = right_child
        if index != max_index:
            self._swap(index, max_index)
            self._sink_down(max_index)
        return

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1
        parent_index = self._parent(index)
        while index > 0 and self.heap[parent_index] < self.heap[index]:
            self._swap(parent_index, index)
            index = parent_index
            parent_index = self._parent(index)

    def remove(self):
        if len(self.heap) == 0:
            return None
        self._swap(0, len(self.heap) - 1)
        max_value = self.heap.pop()
        self._sink_down(0)
        return max_value


class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _sink_down(self, index):
        min_index = index
        left_child = self._left_child(index)
        right_child = self._right_child(index)
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[min_index]:
            min_index = left_child
        if (
            right_child < len(self.heap)
            and self.heap[right_child] < self.heap[min_index]
        ):
            min_index = right_child
        if index != min_index:
            self._swap(index, min_index)
            self._sink_down(min_index)
        return

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1
        parent_index = self._parent(index)
        while index > 0 and self.heap[parent_index] > self.heap[index]:
            self._swap(parent_index, index)
            index = parent_index
            parent_index = self._parent(index)

    def remove(self):
        if len(self.heap) == 0:
            return None
        self._swap(0, len(self.heap) - 1)
        min_value = self.heap.pop()
        self._sink_down(0)
        return min_value
