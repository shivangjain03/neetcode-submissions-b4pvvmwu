class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(s):
            return s == s[::-1]
        def dfs(i,curr):
            if i >= len(s):
                res.append(curr.copy())
                return
            for j in range(i,len(s)):
                if isPalindrome(s[i:j+1]):
                    curr.append(s[i:j+1])
                    dfs(j + 1, curr)
                    curr.pop()
        dfs(0,[])
        return res        