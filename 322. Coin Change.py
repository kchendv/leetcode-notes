class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        a = dict()
        a[0] = 0
        for i in range(1, amount + 1):
            if i in coins:
                a[i] = 1
            else:
                possible = []
                for n in coins:
                    if i > n and a[i - n] != -1:
                        possible.append(a[i - n])
                if not possible:
                    a[i] = -1
                else:
                    a[i] = 1 + min(possible)
        if amount in a:
            return a[amount]
        return -1
