class Solution:
    def hammingWeight(self, n: int) -> int:
        # Using n&(n-1) way
        count = 0
        while n>0:
            n&=(n-1)
            count+=1
        return count
        