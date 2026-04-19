class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Brute force: O(n^2)
        res = -1000
        for i in range(len(nums)):
            curr = 0
            for j in range(i,len(nums)):
                curr = curr+nums[j]
                res = max(curr,res)
        return res        