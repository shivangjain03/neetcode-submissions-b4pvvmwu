class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        st = ""
        def dfs(open_count,close_count, st):
            if open_count == close_count == n:
                res.append(st)
            if open_count<n:
                dfs(open_count+1,close_count,st+"(")
            if close_count<open_count:
                dfs(open_count, close_count+1, st+")")
        dfs(0,0,"")
        return res
            
        