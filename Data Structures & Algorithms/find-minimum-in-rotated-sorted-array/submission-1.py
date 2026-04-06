class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Brute force
        #O(n)
        """min = nums[0]
        for i in nums:
            if i<min:
                min = i
        return min"""

        #O(n)
        nums.sort()
        return nums[0]            



        