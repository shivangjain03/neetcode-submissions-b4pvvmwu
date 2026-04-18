class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2":'abc', "3":'def', "4":'ghi', "5":'jkl', "6":'mno', "7":'pqrs', "8":'tuv', "9":'wxzy'}
        res = []
        def dfs(i,st):
            if not digits:
                return []        
            else:
                if len(st) == len(digits):
                    res.append(st)
                    return
                letters = dic[digits[i]]
                for j in letters:
                    dfs(i+1,st+j)
        dfs(0,"")
        return res
                
                



        