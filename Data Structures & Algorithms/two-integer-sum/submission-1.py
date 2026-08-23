class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited= {}

        for i, value in enumerate(nums):
            difference = target - value
            if difference in visited:
                return [visited[difference], i]
            visited[value] = i