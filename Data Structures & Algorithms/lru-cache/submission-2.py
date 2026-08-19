class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mem_dict = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.mem_dict:
            return -1
        else:
            self.mem_dict.move_to_end(key)
            return self.mem_dict[key]
        
    def put(self, key: int, value: int) -> None:
        if key in self.mem_dict:
            self.mem_dict.move_to_end(key)
            self.mem_dict[key] = value
        elif len(self.mem_dict)< self.capacity:
            self.mem_dict[key] = value
        else:
            self.mem_dict.popitem(last=False)
            self.mem_dict[key] = value