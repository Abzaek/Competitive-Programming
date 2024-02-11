class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        lookup = defaultdict(int)
        l = 0
        r = 0
        _max = float('-inf')

        while r < len(fruits):
            lookup[fruits[r]] += 1

            while len(lookup) > 2:
                lookup[fruits[l]] -= 1
                if lookup[fruits[l]] == 0:
                    del lookup[fruits[l]]
                l += 1
            
            _max = max(r - l + 1, _max)

            r += 1

        return _max