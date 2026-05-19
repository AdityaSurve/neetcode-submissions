class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        stack = set()
        for i in nums:
            if i in stack:
                return True
            else:
                stack.add(i)
        return False