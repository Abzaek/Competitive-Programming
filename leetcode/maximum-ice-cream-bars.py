class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        _min = float('inf')
        _max = float('-inf')
        _count = 0

        for i in costs:
            _min = min(i, _min)
            _max = max(i, _max)
        
        storageArr = [0]*(_max - _min + 1)

        for i in costs:
            storageArr[i - _min] += 1
        
        for i in range(len(storageArr)):
            if storageArr[i] != 0:
                if coins - storageArr[i]*(i+_min) >= 0:
                    coins -= (i+_min)*storageArr[i]
                    _count += storageArr[i]
                
                else:
                    for j in range(storageArr[i]):
                        if coins - (i+_min) >= 0:
                            coins -= (i+_min)
                            _count += 1
                        else:
                            break

        return _count





        