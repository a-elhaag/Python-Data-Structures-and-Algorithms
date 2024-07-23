# this is a comment


class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return True
        new_node = Node(value)
        current = self.root
        while True:
            if value == current.value:
                return False
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return True
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return True
                current = current.right

    def contains(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def _r_contains(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._r_contains(node.left, value)
        return self._r_contains(node.right, value)

    def r_contains(self, value):
        return self._r_contains(self.root, value)

    def _r_insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._r_insert(node.left, value)
        elif value > node.value:
            node.right = self._r_insert(node.right, value)
        return node

    def r_insert(self, value):
        self.root = self._r_insert(self.root, value)
        return True

    def min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value

    def _delete_node(self, node, value):
        current_node = node
        if current_node is None:
            return False

        if value < current_node.value:
            current_node.left = self._delete_node(current_node.left, value)

        elif value > current_node.value:
            current_node.right = self._delete_node(current_node.right, value)

        else:
            if current_node.left is None and current_node.right is None:
                return None
            if current_node.left is None:
                return current_node.right
            if current_node.right is None:
                return current_node.left

            else:
                min_value = self.min_value(current_node.right)
                current_node.value = min_value
                current_node.right = self._delete_node(current_node.right, min_value)

        return current_node

    def delete_node(self, value):
        self.root = self._delete_node(self.root, value)
