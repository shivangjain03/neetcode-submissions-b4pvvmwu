class Solution:
    def isPalindrome(self, s: str) -> bool:
        l =[]
        for i in s:
            if i.isalnum():
                l.append(i.lower())
        print(l)
        print(l[::-1])
        return l == l[::-1]
        