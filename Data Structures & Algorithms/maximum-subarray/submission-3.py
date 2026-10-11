class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Brute Force
        """max_sum = float('-inf')
        for i in range(len(nums)):
            temp_sum = 0
            for j in range(i, len(nums)):
                temp_sum += nums[j]
                if temp_sum > max_sum:
                    max_sum = temp_sum
        return max_sum """

        #Kadane's Algorithm
        currSum = 0
        maxSum = -float('inf')
        for i in nums:
            
            if currSum<0:
                currSum = 0
            
            currSum+=i
            
            maxSum = max(currSum, maxSum)
        return maxSum
            

