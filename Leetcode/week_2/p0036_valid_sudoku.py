from typing import List


class Solution:
    def isValidSudoku_one_pass(self, board: List[List[str]]) -> bool:
        """
        m = row len, n = col len
        One pass solution O(mn)
        Space O(n + mn/3 + mn)
        """

        row_set = set()
        block_3x3_set = [set() for _ in range(3)]
        col_set = [set() for _ in range(len(board))]

        for i, row in enumerate(board):
            row_set = set()  # reset row set every row
            if i % 3 == 0:    # reset 3x3 block set every 3 rows
                block_3x3_set = [set() for _ in range(3)]
            for j, num in enumerate(row):
                if num == '.':
                    continue

                # check row
                if num in row_set:
                    return False
                row_set.add(num)

                # check 3x3 block
                if num in block_3x3_set[j // 3]:
                    return False
                block_3x3_set[j // 3].add(num)

                # check col
                if num in col_set[j]:
                    return False
                col_set[j].add(num)

        return True


"""
Runtime: O(mn)
Space: O(n + mn/3 + mn)
Where m = no of rows and n = no of cols

Runtime: 84 ms, faster than 99.39% of Python3 online submissions for Valid Sudoku.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Valid Sudoku.
"""
