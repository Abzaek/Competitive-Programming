class Solution(object):
    def longestCommonPrefix(self, strs):
        longestCommonPrefix = ""
        if strs is None or len(strs) == 0:
            return longestCommonPrefix
        
        minimumLength = len(strs[0])
        for i in range(1, len(strs)):
            minimumLength = min(minimumLength, len(strs[i]))
        
        for i in range(minimumLength):
            current = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != current:
                    return longestCommonPrefix
            longestCommonPrefix += current
        
        return longestCommonPrefix
        