class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove space out of string and compare lower cases to all
        # pointer1 = 0
        # pointer2 = len(s)-1
        newStr = ''
        for c in s: 
            if c.isalnum():
                newStr += c.lower()

        return newStr == newStr[::-1]

