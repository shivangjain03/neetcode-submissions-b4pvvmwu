class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index,total,current_list):
            if total==target:
                res.append(current_list.copy())
                return
            if index==len(nums) or total>target:
                return
            
            current_list.append(nums[index])
            dfs(index,total+nums[index], current_list)
            current_list.pop()
            dfs(index+1,total, current_list)
        dfs(0,0,[])
        return res
        