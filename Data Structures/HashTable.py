class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        hash = 0
        for letter in key:
            hash = (hash + ord(letter) * 23) % len(self.data_map)
        return hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if not self.data_map[index]:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]:
            for item in self.data_map[index]:
                if item[0] == key:
                    return item[1]
        return None

    def keys(self):
        keys = []
        for item in self.data_map:
            if item:
                for key, value in item:
                    keys.append(key)
        return keys
