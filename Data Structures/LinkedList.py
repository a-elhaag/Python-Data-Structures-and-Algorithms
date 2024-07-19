class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
            return
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def pop(self):
        if self.head is None:
            return None

        temp = self.head
        if self.head.next is None:
            self.head = None
            self.tail = None
            self.length = 0
            return temp.data

        while temp.next.next is not None:
            temp = temp.next

        val = temp.next.data
        temp.next = None
        self.tail = temp
        self.length -= 1
        return val

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            self.length = 1
            return
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.head is None:
            return None

        temp: Node = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.data

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp is None:
            return False
        temp.data = value
        return True

    def insert(self, index, value):
        if index == self.length:
            self.append(value)
            return True
        temp = self.get(index)
        if temp is None:
            return False
        if index == 0:
            self.prepend(value)
            return True
        new_node = Node(value)
        new_node.next = temp
        temp = self.get(index - 1)
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        temp = self.get(index)
        if temp is None:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.data

    def reverse(self):
        if self.length == 1:
            return
        first = self.head
        self.tail = self.head
        second = first.next
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
