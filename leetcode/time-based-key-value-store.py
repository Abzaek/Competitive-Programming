class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        
        l = -1
        r = len(self.storage[key])
        while l + 1 < r:
            mid = l + (r - l)//2

            if self.storage[key][mid][1] > timestamp:
                r = mid
            elif self.storage[key][mid][1] <= timestamp:
                l = mid
        return self.storage[key][l][0] if l != -1 else ''

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)