class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hash_table = {}
        ans = []
        for i in cpdomains:
            temp_array = i.split(' ')
            
            dom = temp_array[1].split('.')
            if temp_array[1] not in hash_table:
                hash_table[temp_array[1]] = int(temp_array[0])
            else:
                hash_table[temp_array[1]] += int(temp_array[0])
            if len(dom) == 3:
                if dom[2] not in hash_table:
                    hash_table[dom[2]] = int(temp_array[0])
                else:
                    hash_table[dom[2]] += int(temp_array[0])
                if (dom[1] + '.' + dom[2]) not in hash_table:
                    hash_table[dom[1] + '.' + dom[2] ] = int(temp_array[0])
                else: 
                    hash_table[dom[1] + '.' + dom[2] ] += int(temp_array[0])
            else:
                if dom[1] not in hash_table:
                    hash_table[dom[1]] = int(temp_array[0])
                else:
                    hash_table[dom[1]] += int(temp_array[0])
                    
        for c, k in hash_table.items():
            ans.append(str(k) + " " + c)
        return ans
