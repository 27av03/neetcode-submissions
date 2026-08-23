class Solution:
    def hasDuplicate(self, nums) -> bool:
        return len(set(nums)) < len(nums)
        