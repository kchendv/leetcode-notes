class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) == 1: return 0
        stockPrices.sort()
        lasty = stockPrices[1][1] - stockPrices[0][1]
        lastx = stockPrices[1][0] - stockPrices[0][0]
        lines = 1
        for i in range(1, len(stockPrices)-1):
            p1 = stockPrices[i]
            p2 = stockPrices[i+1]
            if lastx * (p2[1] - p1[1]) != lasty * (p2[0] - p1[0]):
                lines += 1
                lastx = (p2[0] - p1[0])
                lasty = (p2[1] - p1[1])
        return lines