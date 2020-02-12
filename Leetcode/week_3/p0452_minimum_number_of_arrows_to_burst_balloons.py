from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        return self.verbose_sorted_soln(points)

    def verbose_sorted_soln(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        elif len(points) == 0:
            return 0

        points.sort()
        arrows = 1
        last_end = points[0][1]
        last_shot = points[0][1]  # the last shot that was taken

        for point in points:
            start, end = point
            new_arrow = False

            if start <= last_end:     # same arrow might be used
                # [1,2],[1,3],[3,10] here when iter is at [3,10], start <= last_end (3 <= 3)
                # however, last_shot was at 2 and start > last_shot is true (3 > 2) so we need
                # a new arrow
                if start > last_shot:
                    new_arrow = True
                last_shot = min(last_shot, end)  # for cases like [1,10],[3,9]
            else:
                new_arrow = True

            if new_arrow:
                arrows += 1
                last_shot = end

            last_end = end

        return arrows


"""
Runtime: O(nlogn)
Space: O(1)

Runtime: 460 ms, faster than 48.83% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.
Memory Usage: 18 MB, less than 16.67% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.
"""
