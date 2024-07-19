class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self, data):
        self.head = self.tail = Node(data)

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, data):
        self.length += 1
        if self.head is None:
            self.head = self.tail = Node(data)
            return
        new_node = Node(data)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def pop(self):
        if self.head is None:
            return None
        temp = self.tail
        self.length -= 1

        if self.tail.prev is None:
            self.head = self.tail = None
            return temp

        self.tail = self.tail.prev
        self.tail.next = None
        return temp

    def prepend(self, data):
        if self.length == 0:
            self.head = self.tail = Node(data)
            self.length += 1
            return
        self.length += 1
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def pop_first(self):
        if self.head is None:
            return None

        temp = self.head
        self.length -= 1
        if self.head.next is None:
            self.head = self.tail = None
            return temp
        self.head = self.head.next
        self.head.prev = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.head
        if index == self.length - 1:
            return self.tail
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, data):
        temp = self.get(index)
        if temp is None:
            return False
        temp.value = data
        return True

    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
            return True
        if index == self.length:
            self.append(data)
            return True
        if self.get(index) is None:
            return False
        self.length += 1
        new_node = Node(data)
        temp = self.get(index)
        new_node.next = temp
        new_node.prev = temp.prev
        temp.prev.next = new_node
        temp.prev = new_node
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        self.length -= 1
        return temp
