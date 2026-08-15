class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict_cache = collections.OrderedDict()
        

    def get(self, key: int) -> int:
        if key in self.dict_cache:
            self.dict_cache.move_to_end(key)
            return self.dict_cache[key]
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.dict_cache:
            self.dict_cache.move_to_end(key)
        self.dict_cache[key] = value
        if len(self.dict_cache) > self.capacity:
            self.dict_cache.popitem(last=False)
        

            


        
