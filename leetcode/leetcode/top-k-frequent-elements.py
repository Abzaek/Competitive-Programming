class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      arr = []
      cnt = defaultdict(int)
      _max = -inf

      for num in nums:
        if num not in cnt:
          arr.append(num)
        cnt[num] += 1
        _max = max(cnt[num], _max)
      ans = []
      N = len(arr)
      lookup = [[] for i in range(N)]
      
      for a in arr:
        lookup[N - 1 - math.floor(N*cnt[a]/(_max + 1))].append(a)
        lookup[N - 1 - math.floor(N*cnt[a]/(_max + 1))].sort()
      for ar in lookup:
        ans.extend(ar)
        if len(ans) == k:
          break
      return ans


      



        