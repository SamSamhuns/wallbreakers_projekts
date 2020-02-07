from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return self.bfs(grid)

    def bfs(self, grid: List[List[str]]) -> int:

        self.seen = set()
        islands = 0

        def bfs_spread(coord):
            queue = deque([coord])

            while queue:
                for i in range(len(queue)):
                    x, y = queue.popleft()
                    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        nx, ny = x + dx, y + dy
                        if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[nx]):
                            if grid[nx][ny] == '1' and (nx, ny) not in self.seen:
                                self.seen.add((nx, ny))
                                queue.append((nx, ny))

        for i, row in enumerate(grid):
            for j, elem in enumerate(row):

                if elem == "1" and (i, j) not in self.seen:
                    self.seen.add((i, j))
                    bfs_spread((i, j))
                    islands += 1

        return islands


"""
Runtime O(mn)
Space O(mn)
where m = no of rows and m = no of cols in grid

Runtime: 168 ms, faster than 28.01% of Python3 online submissions for Number of Islands.
Memory Usage: 17.8 MB, less than 5.13% of Python3 online submissions for Number of Islands.
"""
