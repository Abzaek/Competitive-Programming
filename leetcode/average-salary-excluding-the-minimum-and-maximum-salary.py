class Solution:
    def average(self, salary: List[int]) -> float:
        minimum = salary[0]
        maximum = salary[0]
        total = 0
        for i in salary:
            if i < minimum:
                if minimum < maximum:
                    total += minimum
                minimum = i
            elif i > maximum:
                if maximum > minimum:
                    total += maximum
                maximum = i
            elif i > minimum and i < maximum:
                total += i
        ans = total /(len(salary) - 2)
        return ans
        

        
        