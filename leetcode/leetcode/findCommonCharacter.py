class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        _count = Counter(words[0])
        ans = []
        for word in words[1:]:
            curr_count = Counter(word)

            for i in curr_count:
                if i not in _count:
                    continue
                _count[i] = min(_count[i], curr_count[i])
            temp = []
            for i in _count:
                if i not in curr_count:
                    temp.append(i)
                    continue
            for i in temp:
                del _count[i]

        for i in _count:
            for j in range(_count[i]):
                ans.append(i)
        return ans