from typing import List
from collections import defaultdict


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        DP hash map and dfs solution
        Calculate the longest path subproblem at each coord in the matrix
        max_dist_map stores the maximum increasing path at that coord
        Do not start iteration if maximum path exists
        Only iterate to next coord if the maximum path can be increased
        """

        self.max_dist_map = defaultdict(int)
        self.max_dist = 0

        def _max_path_dfs(clength, coord):
            x, y = coord
            self.max_dist_map[coord] = clength
            self.max_dist = max(self.max_dist, clength)
            cnode = matrix[x][y]

            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < len(matrix) and ny >= 0 and ny < len(matrix[nx]):
                    if matrix[nx][ny] > cnode:  # only iterate if next node is greater
                        # only go to next node if path increase
                        if clength + 1 > self.max_dist_map[(nx, ny)]:
                            self.max_dist = max(self.max_dist, clength + 1)
                            _max_path_dfs(clength + 1, (nx, ny))

        for i, row in enumerate(matrix):
            for j, elem in enumerate(row):
                # prevents researching of paths as researching starts at lowest value 1
                if (i, j) not in self.max_dist_map:
                    _max_path_dfs(1, (i, j))

        return self.max_dist


"""
Runtime: 664 ms, faster than 18.85% of Python3 online submissions for Longest Increasing Path in a Matrix.
Memory Usage: 18.8 MB, less than 7.69% of Python3 online submissions for Longest Increasing Path in a Matrix.
"""
