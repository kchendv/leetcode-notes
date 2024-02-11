class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        if len(special) == 0:
            return bottom - top + 1
        dist = [special[0] - bottom, top - special[-1]]
        for n in range(1, len(special)):
            dist.append(special[n] - special[n-1] - 1)
            
        return max(dist)
        