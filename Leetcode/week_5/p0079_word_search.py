from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_start_locs = []
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char == word[0]:
                    word_start_locs.append((i, j))

        if not word_start_locs:
            return False

        def _dfs_backtrack_check(word_idx, coord, seen):
            if word_idx == len(word):
                return True
            x, y = coord
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[nx]):
                    if board[nx][ny] == word[word_idx] and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        found_status = _dfs_backtrack_check(
                            word_idx + 1, (nx, ny), seen)
                        if found_status:
                            return True
                        seen.remove((nx, ny))  # backtracking step

            return False

        for x, y in word_start_locs:
            seen = set()
            seen.add((x, y))
            if _dfs_backtrack_check(1, (x, y), seen):
                return True

        return False


"""
Runtime: 340 ms, faster than 75.58% of Python3 online submissions for Word Search.
Memory Usage: 14 MB, less than 95.74% of Python3 online submissions for Word Search.
"""
