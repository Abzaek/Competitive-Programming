class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l = 0
        r = len(people) -1
        ans = 0

        while r >= l:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
                ans += 1
            elif people[r] <= limit:
                r -= 1
                ans += 1
        return ans



        