class OrderedStream:

    def __init__(self, n: int):
        self.lst = [0]*n
        self.pointer = 0 
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.lst[idKey - 1] = value
        arr = []
        if self.pointer == idKey - 1:
            while self.pointer < len(self.lst) and self.lst[self.pointer] != 0:
                arr.append(self.lst[self.pointer])
                self.pointer += 1
        return arr


        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)