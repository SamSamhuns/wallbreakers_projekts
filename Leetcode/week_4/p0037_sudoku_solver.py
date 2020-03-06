from typing import List
from collections import defaultdict


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_space, col_space, block_space = self.generate_num_dicts(board)
        board_set = [row_space, col_space, block_space]
        self.soln_found = [False]
        self.recursive_fill(0, 0, board, board_set)

    def recursive_fill(self, r, c, board, board_set):
        """
        r,c determines the start position of the next iteration
        instead of starting from the begginning again
        """
        if self.soln_found[0]:
            return

        for i in range(r, len(board)):
            for j in range(c, len(board)):
                c = 0  # restart next iteration from next row
                if board[i][j] == '.':
                    for n in range(1, 10):
                        n = str(n)

                        if self.is_valid((i, j), n, board_set):
                            board[i][j] = n
                            board_set[0][i].add(n)
                            board_set[1][j].add(n)
                            board_set[2][((i // 3) * 3) + (j // 3)].add(n)
                            self.recursive_fill(i, j, board, board_set)
                            # backtrack if final solution hasn't been reached yet
                            # if the solution was found, do not remove the elems
                            if self.soln_found[0]:
                                return
                            board[i][j] = '.'
                            board_set[0][i].remove(n)
                            board_set[1][j].remove(n)
                            board_set[2][((i // 3) * 3) + (j // 3)].remove(n)
                    return  # if no nums were valid, return
        self.soln_found[0] = True

    def is_valid(self, coord, num, board_set):
        r, c = coord
        row_space, col_space, block_space = board_set
        if num in row_space[r] or num in col_space[c] or num in block_space[((r // 3) * 3) + (c // 3)]:
            return False
        return True

    def generate_num_dicts(self, board):
        row_space = defaultdict(set)
        col_space = defaultdict(set)
        block_space = defaultdict(set)

        for i, row in enumerate(board):
            _ = [row_space[i].add(n) for n in row if n != '.']
            for j, elem in enumerate(row):

                r_block_idx = (i // 3) * 3
                c_block_idx = (j // 3)

                if elem != '.':
                    col_space[j].add(elem)
                    block_space[r_block_idx + c_block_idx].add(elem)
        return row_space, col_space, block_space


"""
Runtime: 292 ms, faster than 48.79% of Python3 online submissions for Sudoku Solver.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Sudoku Solver.
"""
