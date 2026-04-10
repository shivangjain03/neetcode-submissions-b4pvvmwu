class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        res1 = Counter(s1)
        l1 = len(s1)
        for i in range(0,len(s2)):
            res2 = Counter(s2[i:i+l1])
            if res1 == res2:
                return True
        
        return False
        