class FrequencyTracker:

    def __init__(self):
        self.count = defaultdict(int)
        self.frequency = defaultdict(int)

    def add(self, number: int) -> None:
        self.count[number] += 1
        if self.frequency[self.count[number] - 1] != 0:
            self.frequency[self.count[number] - 1] -= 1            
        self.frequency[self.count[number]] += 1
    def deleteOne(self, number: int) -> None:
        if self.count[number] != 0:
            self.count[number] -= 1
            self.frequency[self.count[number]] += 1
            self.frequency[self.count[number] + 1] -= 1
            print(self.frequency, self.count)
        
    def hasFrequency(self, frequency: int) -> bool:
        if self.frequency[frequency] != 0:
            return True
        return False
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)