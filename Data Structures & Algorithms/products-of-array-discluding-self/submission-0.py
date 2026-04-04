class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute force method
        # Time comlexity O(n^2) but we need O(n^2)
        output = []
        for i in range(len(nums)):
            calc = 1
            for j in range(len(nums)):
                if i!=j:
                    calc*=nums[j]
            output.append(calc)
        return output




