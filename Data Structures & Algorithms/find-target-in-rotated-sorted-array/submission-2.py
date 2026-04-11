class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (high+low)//2
            if nums[mid] == target:
                return mid

            #If left is sorted
            if nums[mid]>=nums[low]:
                if nums[low]<=target<=nums[mid]:
                    high = mid-1
                else:
                    low = mid+1

            # If right is sorted
            else:
                if nums[mid+1]<=target<=nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1



        