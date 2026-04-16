class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        dic= {}
        
        def dfs(index,total,current):
            if total == target:
                res.append(current.copy())
                return
            if index==len(candidates) or total>target:
                return
            
            current.append(candidates[index])
            dfs(index+1, total+candidates[index],current)

            current.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index+=1
            dfs(index+1,total,current)
        dfs(0,0,[])
        return res
            

        
        