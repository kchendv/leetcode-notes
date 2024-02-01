class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        a = []
        for i, v in enumerate(capacity):
            a.append(v-rocks[i])
        a.sort()
        i = 0
        while i < len(capacity):
            additionalRocks -= a[i]
            if additionalRocks < 0:
                break
            i += 1
        return i