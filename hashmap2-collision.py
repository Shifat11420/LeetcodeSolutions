class HashTable():
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for ch in key:
            hash += ord(ch)
        return hash % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if len(element)== 2 and element[0] == key:
                self.arr[h][index] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key, val))   

    def __getitem__(self, key):
        h = self.get_hash(key)
        for kv in self.arr[h]:
            if kv[0] == key:
                return kv[1]

    def delitem(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                print("Deleting ", index)
                del self.arr[h][index]


if __name__ == '__main__':
    t = HashTable()
    print(t.get_hash("march 6"))
    print(t.get_hash("march 17"))
    t["march 1"] = 10
    t["march 6"] = 310
    t["march 7"] = 420
    t["march 8"] = 67
    t["march 17"] = 63457
    print(t["march 6"])
    print(t.arr)