class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(open_count,closed_count,st):
            if open_count==closed_count==n:
                res.append(st)
            if open_count<n:
                dfs(open_count+1, closed_count, st+"(")
            if open_count>closed_count:
                dfs(open_count,closed_count+1,st+")")
        
        dfs(0,0,"")
        return res

        