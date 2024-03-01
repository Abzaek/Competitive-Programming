class Solution:
    def partitionLabels(self, s: str) -> List[int]:
      
        lookup = defaultdict(list)

        for i in range(len(s)):
            if len(lookup[s[i]]) == 2:
                lookup[s[i]].pop()
                lookup[s[i]].append(i)
            else:
                lookup[s[i]].append(i)
        count = []

        pointer = 0
        values = list(lookup.values())
        while pointer < len(values):
            left = values[pointer][0]
            right = values[pointer][-1]
            while pointer < len(values) and values[pointer][0] <= right:
                right = max(values[pointer][-1], right) 
                pointer += 1
            

            count.append(right - left + 1)
                
                
        return count