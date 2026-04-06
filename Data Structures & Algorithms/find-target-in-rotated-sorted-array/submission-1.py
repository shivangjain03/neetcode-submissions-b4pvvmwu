class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Brute force
        # O(n)
        """for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1"""

        #Hint: O(log n)
        # Normal sort: O(n)-> So no
        # Binary search
        l = 0
        r = len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            #Check if left half is sorted and target<mid
            if nums[l]<=nums[m]:
                if nums[l]<=target and nums[m]>target:
                    r = m-1
                else:
                    l = m+1
            # Check if right is sorted and 
            else:
                if nums[m]<target and target<=nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1

        

