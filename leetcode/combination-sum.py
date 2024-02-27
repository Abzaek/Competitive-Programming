class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        lookup = set()

        def backtrack(candid_sum, candidate, visited):
            if candid_sum == target:
                if tuple(sorted(visited)) not in lookup:
                    ans.append(candidate.copy())
                    lookup.add(tuple(sorted(visited)))
            for i in range(len(candidates)):
                if candid_sum + candidates[i] > target:
                    return
                else:
                    visited.append(i)
                    candidate.append(candidates[i])
                    backtrack(candid_sum + candidates[i], candidate, visited)
                    candidate.pop()
                    visited.pop()
        
        backtrack(0, [], [])
        return ans
        