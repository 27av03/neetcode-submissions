class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, value in enumerate(nums):
            rem = target - value
            if rem in seen:
                return [seen[rem], i]
            seen[value] = i