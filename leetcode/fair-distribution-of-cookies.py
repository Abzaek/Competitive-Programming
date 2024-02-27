class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        if k == len(cookies):
            return max(cookies)
        
        buckets = [0]*k
        min_unfairness = [float('inf')]

        def backtrack(index):
            if index == len(cookies):
                min_unfairness[0] = min(max(buckets), min_unfairness[0])
                return

            for i in range(k):
                buckets[i] += cookies[index]
                if max(buckets) < min_unfairness[0]: backtrack(index + 1) 
                buckets[i] -= cookies[index]

        backtrack(0)
        return min_unfairness[0]



        