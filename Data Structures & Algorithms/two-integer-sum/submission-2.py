class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i, values in enumerate(nums):
            diff = target - values
            if diff in visited:
                return [visited[diff], i]
            visited[values] = i