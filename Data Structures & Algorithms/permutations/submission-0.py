class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = [False]*len(nums)
        current = []
        def dfs():
            if len(current) == len(nums):
                res.append(current.copy())
                return
            
            for i in range(len(nums)):
                if seen[i] != True:
                    current.append(nums[i])
                    seen[i] = True
                    dfs()
                    seen[i] = False
                    current.pop()
        dfs()
        return res
        