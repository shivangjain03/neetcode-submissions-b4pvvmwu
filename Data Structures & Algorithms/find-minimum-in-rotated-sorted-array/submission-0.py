class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Brute force
        min = nums[0]
        for i in nums:
            if i<min:
                min = i
        return min


        