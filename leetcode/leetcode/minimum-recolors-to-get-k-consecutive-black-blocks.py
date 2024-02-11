class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        '''
        initialize l, r, _count, max_count

        '''

        l = 0
        r = 0
        _count = 0

        while r < k:
            if blocks[r] == 'W':
                _count += 1
            r += 1
        
        min_count = _count

        while r < len(blocks):
            if blocks[r] == 'W':
                _count += 1
            if blocks[l] == 'W':
                _count -= 1
            l += 1
            r += 1

            min_count = min(_count, min_count)
            
        return min_count
        