class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # for this check if the memeber is a start memeber by checking if n-1 is in array
        # If first number then check if additional number are there or not and add them to longest streak
        
        if nums == []:
            return 0
        longest_streak = [1]*len(nums)
        for i in range(len(nums)):
            #Checking if it is start of sequence?
            if (nums[i]-1) not in nums:
                if i < len(nums):
                    increm = nums[i]+1
                    while increm in nums:
                        longest_streak[i]+=1
                        increm+=1
        return max(longest_streak)
