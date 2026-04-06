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
        """nums.sort()
        return nums[0]  """

        # O(log n)
        low = 0
        high = len(nums)-1
        result = nums[0]
        while low<=high:
            if nums[low] < nums[high]:
                result = min(result, nums[low])
                break
            mid = (high+low)//2
            result = min(result,nums[mid])
            if nums[mid]>=nums[low]:
                low = mid+1
            else:
                high = mid-1
        return result





        