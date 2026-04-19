class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jump = 0
        farthest = 0
        curr_jump_end = 0

        for i in range(len(nums)-1):
            farthest = max(farthest,i+nums[i])
            if i==curr_jump_end:
                min_jump+=1
                curr_jump_end = farthest
                 
        return min_jump

            



        