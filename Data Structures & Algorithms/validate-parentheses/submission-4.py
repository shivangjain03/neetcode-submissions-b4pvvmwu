class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {'{':'}', '[':']', '(':')'}
        stack = []
        for i in s:
            if i in dict1 :
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if dict1[stack[-1]] != i:
                    s = stack.pop()
                    print(s)
                    return False
                else:
                    stack.pop()
        print(stack)
        if len(stack) != 0:
            return False
        return True
        