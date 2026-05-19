class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stack = defaultdict(list)

        def formatter(a:int, b:int):
            return [min(a,b),max(a,b)]

        for idx, val in enumerate(nums):
            if val in stack:
                return formatter(idx, stack[val])
            else:
                stack[target-val] = idx