class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
      arr = [i for i in range(len(nums))]
      lookup = defaultdict(int)
      def merge(left_arr, right_arr):
        l = 0
        r = 0
        ans = []
        while l < len(left_arr) and r < len(right_arr):
          if nums[left_arr[l]] <= nums[right_arr[r]]:
            ans.append(left_arr[l])
            l += 1
          else:
            lookup[right_arr[r]] += len(left_arr) - l
            ans.append(right_arr[r])

            r += 1
        while l < len(left_arr):
          ans.append(left_arr[l])
          l += 1
        while r < len(right_arr):
          ans.append(right_arr[r])
          r += 1
        return ans
      def mergeSort(left, right, arr):
        if left == right:
            return [arr[left]]

        mid = left + (right - left) // 2

        left_half = mergeSort(left, mid, arr)
        right_half = mergeSort(mid + 1, right, arr)
      
        return merge(left_half, right_half)

      temp = mergeSort(0, len(nums) - 1, arr)
      print(temp)
      answer = [0]*len(nums)

      for i, item in enumerate(temp):
        answer[item] = i - item + lookup[item]

      return answer





        