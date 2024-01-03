class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        summ = skill[-1] + skill[0]
        ans = 0
        l = 0
        r = len(skill) - 1

        while r > l:
            if skill[r] + skill[l] != summ:
                return -1

            ans += skill[r]*skill[l]
            
            r -= 1
            l += 1

        return ans
       
        