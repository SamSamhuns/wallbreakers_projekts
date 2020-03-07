from typing import List


class Solution:
    def islandPerimeter_elegant(self, grid: List[List[int]]) -> int:
        perimeter = 0

        for r, row in enumerate(grid):
            for c, sec in enumerate(row):
                if sec:
                    for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                        nx, ny = r + dx, c + dy
                        if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[nx]):
                            perimeter += 0 if grid[nx][ny] else 1
                        else:
                            perimeter += 1
        return perimeter


"""
Runtime: O(MN)
Space: O(1)

Runtime: 616 ms, faster than 41.74% of Python3 online submissions for Island Perimeter.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Island Perimeter.
"""
