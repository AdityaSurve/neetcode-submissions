class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stack = defaultdict(list)
        for i in s:
            if i in stack:
                stack[i] += 1
            else:
                stack[i] = 1
        for i in t:
            if not i in stack:
                return False
            else:
                stack[i] -= 1
        for val in stack.values():
            if val != 0:
                return False
        return True