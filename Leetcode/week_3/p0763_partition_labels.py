from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        char_idx = {}  # count start and end indexes of chars in S
        for i, char in enumerate(S):           # O(n) operation
            if char not in char_idx:
                char_idx[char] = [i, i]
            char_idx[char] = [char_idx[char][0], i]

        groups = []
        if len(char_idx) == 1:
            for key in char_idx:
                str_end = char_idx[key]
                return [str_end[1] - str_end[0] + 1]

        intervals = sorted(char_idx.values())  # O(nlogn) operation

        # Merge intervals problem now
        last_start, last_end = intervals[0]

        for interval in intervals[1:]:
            start, end = interval
            if start <= last_end:
                last_end = max(end, last_end)
                continue
            groups.append([last_start, last_end])
            last_start, last_end = interval

        groups.append([last_start, last_end])
        return [end - start + 1 for start, end in groups]


"""
Runtime: O(n + nlogn)
Space: O(n)

Runtime: 36 ms, faster than 78.04% of Python3 online submissions for Partition Labels.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Partition Labels.
"""
