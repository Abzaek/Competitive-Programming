class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        lookup = {}
        candidates.sort()
        def backtrack(index, sm, path):
            if sm == target:
                lookup[tuple(path)] = 0
                return
            if index >= len(candidates) or sm > target:
                return 
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                val = sm + candidates[i]
                backtrack(i + 1, val,path)
                path.pop()
        backtrack(0, 0, [])

        return lookup.keys()

