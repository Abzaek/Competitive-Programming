class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        lookup = {}
        candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        def backtrack(index, sm, path):
            if sm == target and len(path) == k:
                lookup[tuple(path)] = 0
                return
            if len(path) >= k:
                return
            if sm > target:
                return 
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                val = sm + candidates[i]
                backtrack(i + 1, val,path)
                path.pop()
        backtrack(0, 0, [])

        return lookup.keys()
        