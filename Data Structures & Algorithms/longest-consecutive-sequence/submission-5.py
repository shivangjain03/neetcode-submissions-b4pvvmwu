class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_consec = 1
        nums.sort()
        temp_consec = 1
        for i in range(1,len(nums)):
            print(nums[i])
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1]+1:
                temp_consec+=1
            else:
                max_consec = max(max_consec, temp_consec)
                temp_consec = 1
        return max(max_consec, temp_consec)

