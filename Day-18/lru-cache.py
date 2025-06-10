import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        self.map.move_to_end(key)
        return self.map[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map.move_to_end(key)

        self.map[key] = value

        if len(self.map) > self.capacity:
            self.map.popitem(False)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)