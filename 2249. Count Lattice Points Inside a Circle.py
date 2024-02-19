class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        a = dict()
        for c in circles:
            for x in range(c[0] - c[2], c[0] + c[2] + 1):
                for y in range(c[1] - c[2], c[1] + c[2] + 1):
                    if (x,y) not in a:
                        if ((x-c[0])**2 + (y-c[1])**2 <= c[2]**2):
                            a[(x,y)] = 1
        
        return len(a)
        