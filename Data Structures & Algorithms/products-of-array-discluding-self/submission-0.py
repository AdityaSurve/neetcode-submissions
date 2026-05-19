class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prods = [1] * n
        prefix = 1
        for i in range(n):
            prods[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n-1, -1, -1):
            prods[i] *= suffix
            suffix *= nums[i]
        return prods