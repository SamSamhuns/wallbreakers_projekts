from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.bfs(board)

    def dfs(self, board: List[List[str]]) -> None:
        # DFS Solution O(mn) where m = no. of rows and n = no. of cols
        def dfs_find(coord, temp_list, touches_boundary):
            self.seen.add(coord)
            x, y = coord

            for add_x, add_y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = x + add_x, y + add_y
                if (nx, ny) not in self.seen:
                    if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[nx]):
                        if board[nx][ny] == 'O':
                            temp_list.append((nx, ny))
                            dfs_find((nx, ny), temp_list, touches_boundary)
                    else:
                        touches_boundary[0] = True

        flip_list = []
        self.seen = set()

        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                if elem == 'O' and (i, j) not in self.seen:
                    temp_flip_list = [(i, j)]
                    # flag to chk if boundary is touched
                    touches_boundary = [False]
                    dfs_find((i, j), temp_flip_list, touches_boundary)
                    if not(touches_boundary[0]):
                        flip_list.append(temp_flip_list)

        if flip_list != []:
            for flips in flip_list:
                for x, y in flips:
                    board[x][y] = 'X'

    def bfs(self, board: List[List[str]]) -> None:
        seen = set()
        flip_list = []
        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                if elem == 'O' and (i, j) not in seen:
                    seen.add((i, j))
                    queue = deque([(i, j)])
                    temp_flip_list = [(i, j)]
                    touches_boundary = False
                    while queue:
                        for _ in range(len(queue)):
                            x, y = queue.popleft()
                            for ax, ay in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                                nx, ny = x + ax, y + ay
                                if (nx, ny) not in seen:
                                    if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[nx]):
                                        if board[nx][ny] == 'O':
                                            seen.add((nx, ny))
                                            temp_flip_list.append((nx, ny))
                                            queue.append((nx, ny))
                                    else:
                                        touches_boundary = True

                    if not(touches_boundary):
                        flip_list.append(temp_flip_list)

        if flip_list != []:
            for flips in flip_list:
                for x, y in flips:
                    board[x][y] = 'X'


"""
Runtime O(mn)
Space O(mn)
where m = no of rows and n = no of cols in board

Runtime: 200 ms, faster than 24.00% of Python3 online submissions for Surrounded Regions.
Memory Usage: 20.7 MB, less than 6.67% of Python3 online submissions for Surrounded Regions.
"""
