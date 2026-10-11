class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {'{':'}', '(':')', '[':']'}
        stack = []
        for i in s:
            if i in dict1:
                stack.append(i)
            else:
                if stack and dict1[stack.pop()] == i:
                    continue
                else:
                    return False
        return len(stack) == 0
