class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        a = dict()
        
        for n in nums:
            for i in n:
                if i not in a:
                    a[i] = 0
                a[i] += 1
        
        s = []
        l = len(nums)
        for i in range(1,1001):
            if i in a and a[i] == l:
                s.append(i)
            
        return s
        