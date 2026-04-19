class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Brute force: O(n^2)
        """res = -1000
        for i in range(len(nums)):
            curr = 0
            for j in range(i,len(nums)):
                curr = curr+nums[j]
                res = max(curr,res)
        return res  """ 

        #Using Kadane's Algo
        # Time complexity = O(n)
        res = nums[0]
        curr = nums[0]
        for i in range(1, len(nums)):
            curr = max(curr+nums[i],nums[i])
            res = max(res,curr)
        return res
