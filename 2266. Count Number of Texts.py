class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        memo = dict()
        memo[len(pressedKeys)] = 1
        for n in range(len(pressedKeys) - 1, -1, -1):
            sub = pressedKeys[n:]
            answers = 0
            q = len(sub)
            if q >= 4 and (sub[0:4] == '7777' or sub[0:4] == '9999'):
                answers = memo[n + 1] + memo[n + 2] + memo[n + 3] + memo[n + 4] 
            elif q >= 3 and (sub[0] == sub[1] and sub[1] == sub[2]):
                answers = memo[n + 1] + memo[n + 2] + memo[n + 3]
            elif q >= 2 and (sub[0] == sub[1]):
                answers = memo[n + 1] + memo[n + 2]
            elif q >= 1:
                answers = memo[n + 1]
            # print("X",sub, answers % 1000000007)
                    
            memo[n] = answers % 1000000007
        return memo[0] % 1000000007
        