class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove space out of string and compare lower cases to all
        # pointer1 = 0
        # pointer2 = len(s)-1
        i = 0
        j = len(s)-1
        while(i<j):
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() == s[j].lower():
                    i = i+1
                    j=j-1
                    continue
                else:
                    return False
            else:
                if s[i].isalnum() and not s[j].isalnum():
                    j=j-1
                else:
                    i=i+1
        return True

