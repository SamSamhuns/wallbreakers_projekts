from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        elif len(intervals) == 1:
            return intervals

        intervals.sort()
        last_start, last_end = intervals[0]
        combined_intervals = []

        for interval in intervals[1:]:
            start, end = interval
            if start <= last_end:
                last_end = max(last_end, end)
                continue
            combined_intervals.append([last_start, last_end])
            last_start, last_end = interval

        combined_intervals.append([last_start, last_end])

        return combined_intervals


"""

"""
