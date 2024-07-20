class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, data):
        self.first = self.last = Node(data)
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def dequeue(self):
        if self.first is None:
            return None
        temp = self.first
        self.length -= 1
        if self.first.next is None:
            self.first = self.last = None
            return temp
        self.first = self.first.next
        return temp

    def enqueue(self, data):
        self.length += 1
        new_node = Node(data)
        if self.first is None:
            self.first = self.last = new_node
            return
        self.last.next = new_node
        self.last = new_node
