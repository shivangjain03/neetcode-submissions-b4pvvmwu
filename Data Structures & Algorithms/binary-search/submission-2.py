class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Brute Force
        """if target in nums:
            return nums.index(target)
        else:
            return -1"""

        #using binary search
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                low = mid+1
            else:
                high = mid-1
        return -1

        
        