class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # options = delete, replace, insert
        #
        # example: word1 = "horse", word2 = "ros"
        #
        # intuition: if two letters are not equal at a given step
        #            we always do a replacement
        #
        #      ""  h ho hor hors horse
        #   ""  0  1  2   3    4     5
        #   r   1  1  2   2    3     4
        #  ro   2  2  1   2    3     4
        # ros   3  3  2   3    2     3

        dp_arr = [[i + j for j in range(len(word1) + 1)]
                  for i in range(len(word2) + 1)]

        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp_arr[i][j] = dp_arr[i - 1][j - 1]
                else:
                    dp_arr[i][j] = min(
                        dp_arr[i][j - 1], dp_arr[i - 1][j], dp_arr[i - 1][j - 1]) + 1

        return dp_arr[-1][-1]


"""
Runtime: O(n^2)
Space: O(n^2)

Runtime: 200 ms, faster than 46.47% of Python3 online submissions for Edit Distance.
Memory Usage: 21.5 MB, less than 7.69% of Python3 online submissions for Edit Distance.
"""
