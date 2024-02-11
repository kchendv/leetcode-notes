class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        a = max(candidates)
        count = 1
        b = 1
        while a > b:
            b <<= 1
            count += 1
        
        c = []
        for i in range(count):
            d = 0
            for num in candidates:
                d += 1 if (((1 << i) & num) > 0) else 0 
            c.append(d)
        return max(c)