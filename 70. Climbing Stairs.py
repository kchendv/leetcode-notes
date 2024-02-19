class Solution:
    def climbStairs(self, n: int) -> int:
        q = {1:1, 2:2}
        for i in range(3, n+1):
            q[i] = q[i-1] + q[i-2]
        return q[n]