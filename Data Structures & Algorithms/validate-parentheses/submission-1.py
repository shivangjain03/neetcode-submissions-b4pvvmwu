class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return True
        match = {'{':'}', '[':']', '(':')'}
        se= []
        for i in s:
            # Checking if it is a opening bracket
            if i in match:
                se.append(i)
            #Checking if it is a closing bracket
            else:
                if not se or i != match[se.pop()]:
                    return False
        return len(se)==0

              