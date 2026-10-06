class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # access each interval in the list
        # store start and end value --> for start, end in interval[i]
        # check if the end is greater or equal to the next intervals start time
        # if yes, merge the two intervals --> [start_i, end_i+1]
        # after merging, pop interval[i] from the list to remove it in O(1) time
        # if no merge, leave the interval untouched
        # return the array

        intervals.sort()

        # "I start my result with the first interval, so there's always a 'last kept' one to compare with."
        merged = [intervals[0]]

        # "Now I walk through the rest, unpacking each into start and end."
        for start, end in intervals[1:]:
            # "If this interval starts at or before the end of the last one I kept, they overlap.
            #  I'm using <= because you said touching counts."
            if start <= merged[-1][1]:
                # "To merge, I keep the earlier start and take the BIGGER end, because one
                #  interval can sit completely inside another, like [1,10] and [2,3]."
                merged[-1][1] = max(merged[-1][1], end)
            else:
                # "Otherwise there's a gap, so this one starts a new interval."
                merged.append([start, end])

        # "Finally I return the merged list."
        return merged

