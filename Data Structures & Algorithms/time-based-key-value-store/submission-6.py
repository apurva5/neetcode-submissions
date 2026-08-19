class TimeMap:
    def __init__(self):
        self.time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key]=[]
        self.time_map[key].append([value,timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.time_map:
            return ""
        left = 0 
        
        value = self.time_map[key]
        right = len(value) - 1
        while left <= right:
            mid = (right+left)//2
            if value[mid][1]<=timestamp:
                res = value[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res

        
