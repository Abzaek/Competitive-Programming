class RecentCounter:

    def __init__(self):
        self.queue = []
        self.index = 0
    def ping(self, t: int) -> int:
        self.queue.append(t)
        if t <= 3000:
            return len(self.queue)
        while t - self.queue[self.index] > 3000:
            self.index += 1
        self.queue = self.queue[self.index:]
        self.index = 0
        return len(self.queue) 


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)