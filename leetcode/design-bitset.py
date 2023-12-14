class Bitset:

    def __init__(self, size: int):
        self.bitset = ["0"]*size
        self.bitset2 = ["1"]*size
        self.counter = {0:size, 1:0}
        self.size = size

    def fix(self, idx: int) -> None:
        if self.bitset[idx] != '1':
            self.bitset[idx] = '1'
            self.bitset2[idx] = '0'
            self.counter[0] -= 1
            self.counter[1] += 1
        
    def unfix(self, idx: int) -> None:
        if self.bitset[idx] != '0':
            self.bitset[idx] = '0'
            self.bitset2[idx] = '1'
            self.counter[0] += 1
            self.counter[1] -= 1

    def flip(self) -> None:
        self.bitset, self.bitset2 = self.bitset2, self.bitset
        self.counter[0], self.counter[1] = self.counter[1], self.counter[0]
        
    def all(self) -> bool:
        return self.counter[1] == self.size

    def one(self) -> bool:
        return self.counter[1] > 0

    def count(self) -> int:
        return self.counter[1]

    def toString(self) -> str:
        return "".join(self.bitset)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()