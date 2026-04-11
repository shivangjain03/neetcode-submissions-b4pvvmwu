class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Brute force
        """mini = 1000
        for i in nums:
            if mini>i:
                mini = i
        return mini"""

        #Rotated array binary search 
        # One half will be sorted the other will have the min

        low = 0
        high = len(nums) - 1
        result = max(nums)
        while low<=high:
            mid = (high+low)//2
            result = min(result,nums[mid])
            if nums[mid]>nums[high]:
                low = mid+1
            else:
                high = mid-1
        return result

        