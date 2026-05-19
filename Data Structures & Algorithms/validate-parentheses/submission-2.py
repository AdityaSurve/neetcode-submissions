class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '[' or ch == '{' or ch == '(':
                stack.append(ch)
            else:
                if stack != [] and ((ch == ']' and stack[-1] == '[') or (ch == '}' and stack[-1] == '{') or (ch == ')' and stack[-1] == '(')):
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        return False