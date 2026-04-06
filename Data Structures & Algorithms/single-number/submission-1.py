class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Brute force
        # Time complex = O(n)
        # Space Complex = O(n)
        """d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        
        for i in d:
            if d[i] == 1:
                return i"""

        #BIT manupalation
        # Space complexity = O(1)
        # Time complexity = O(n)

        res = 0
        for i in nums:
            res^=i
        
        return res
                
        