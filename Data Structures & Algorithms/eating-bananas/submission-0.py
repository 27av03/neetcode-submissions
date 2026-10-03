class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            total = 0
            mid = (right + left) // 2
            for nums in piles:
                total += (nums + mid - 1) // mid
            if total > h:
                left = mid + 1
            else:
                right = mid - 1
        
        return left