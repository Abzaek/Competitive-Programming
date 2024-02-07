class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        '''
        initialize a prefix sum
        initialize a hashmap{alphabet: index} and {index:alphabet}
        iterate over shifts and assign the left index 1 or -1 
        assign at r + 1, 1 or -1 
        finding the prefix sum
        '''
        
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        
        alpha_lookup = {item: i for i, item in enumerate(alpha)}
        
        index_lookup = {i: item for i, item in enumerate(alpha)}
        prefix_sum = [0]*len(s)
        accumulator = 0
        
        s = list(s)
        
        for shift in shifts:
            if shift[1] >= len(s) -1:
                if shift[-1] == 0:
                    prefix_sum[shift[0]] -= 1
                else:
                    prefix_sum[shift[0]] += 1
                continue
            
            if shift[-1] == 0:
                prefix_sum[shift[0]] -= 1
                prefix_sum [shift[1] + 1] += 1
            else:
                prefix_sum[shift[0]] += 1
                prefix_sum [shift[1] + 1] -= 1
        
        for i, item in enumerate(prefix_sum):
            prefix_sum[i] = accumulator + item
            accumulator += item
        
        for i in range(len(s)):
            prefix_sum[i] += alpha_lookup[s[i]]
            
            s[i] = index_lookup[prefix_sum[i] % 26]
        return ''.join(s)
        
        
        
                
        
        