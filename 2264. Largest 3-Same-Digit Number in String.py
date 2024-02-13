class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for n in range(9,-1,-1):
            if str(n)+str(n)+str(n) in num:
                return str(n)+str(n)+str(n)
        return ""