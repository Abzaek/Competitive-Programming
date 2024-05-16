class Solution:
    def bestClosingTime(self, customers: str) -> int:
        yes = [0]*(len(customers) + 1)
        left = 0
        right = 0
        no = [0]*(len(customers) + 1)
        _min = 0
        minP = float('inf')
        for i in range(len(customers)):
            if customers[i] == 'Y':
                yes[i] = left + 1
            else:
                yes[i] = left 
                left += 1
        for i in range(len(customers)- 1, -1,-1):    
            if customers[i] == 'N':
                no[i] = right
            else:
                no[i] = right
                right += 1
        
        if customers[-1] == 'Y':
            yes[-1] = left
        else:
            yes[-1] = left + 1
    
        for i in range(len(customers) + 1):
            if yes[i] + no[i] < minP:
                minP = yes[i] + no[i]
                _min = i

        return _min  
        

