class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            first = target - nums[i]
            if first in dict1:
                return [dict1[first],i]
            else:
                dict1[nums[i]] = i

        