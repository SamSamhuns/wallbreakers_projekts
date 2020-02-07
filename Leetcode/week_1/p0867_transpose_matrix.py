from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return self.manual_transpose(A)

    def manual_transpose(self, A: List[List[int]]) -> List[List[int]]:
        B = [[0] * len(A) for _ in range(len(A[0]))]  # transposed matrix
        for i in range(len(B)):
            for j in range(len(B[i])):
                B[i][j] = A[j][i]  # access transposed coords in A
        return B


"""
Runtime: O(mn)
Space: O(mn)
where m = no of rows in A and n = no of cols in A

Runtime: 72 ms, faster than 80.91% of Python3 online submissions for Transpose Matrix.
Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Transpose Matrix.
"""
