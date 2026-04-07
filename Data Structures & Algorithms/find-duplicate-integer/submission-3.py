class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Brute force
        # Time complexity = O(n)
        # Space complexity = O(n)
        """dictionary = {}
        for i in nums:
            if i in dictionary:
                return i
            else:
                dictionary[i] = 1"""

        # Time complexity = O(n)
        # Space complexity = O(1)
        for i in nums:
            index = abs(i) - 1
            if nums[index]<0:
                return abs(i)
            else:
                nums[index]*=-1
        return -1

        
        