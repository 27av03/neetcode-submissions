class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # Value --> index

        for i, number in enumerate(nums):
            diff = target - number
            if diff in prevMap:
                return [prevMap[diff], i]
            else:
                prevMap[number] = i