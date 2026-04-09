class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time complexity = O(n)
        # Space complexity = O(n)

        output = []
        dict1 = {}
        for i in range(len(nums)):
            second = target - nums[i]
            if second in dict1:
                return [dict1[second],i]
            else:
                dict1[nums[i]] = i

        