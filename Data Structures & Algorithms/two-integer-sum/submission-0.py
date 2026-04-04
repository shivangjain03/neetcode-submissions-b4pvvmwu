class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute force 
        # Time complexity: O(n^2)
        # Initialise a list
        # add 2 iterators i1 and i2
        #Start form index 0 and 1 and increment accordingly
        for i1 in range(len(nums)):
            for i2 in range(len(nums)):
                if nums[i1]+nums[i2] == target and i1!=i2:
                    return [i1,i2]
                      