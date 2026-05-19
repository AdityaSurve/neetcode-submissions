class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        checked_val = defaultdict(bool)
        longest_val = 0
        for num in nums:
            if checked_val[num]:
                continue
            checked_val[num] = True
            val = 1
            left = num-1
            while left in set_nums and not checked_val[left]:
                checked_val[left] = True
                val+=1
                left-=1
            right = num+1
            while right in set_nums and not checked_val[right]:
                checked_val[right] = True
                val+=1
                right+=1
            longest_val = max(longest_val, val)
        return longest_val