class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append(intervals[i])
        return merged