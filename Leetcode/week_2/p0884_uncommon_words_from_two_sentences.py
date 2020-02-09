from typing import List
from collections import Counter


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A_ctn = Counter(A.split())
        B_ctn = Counter(B.split())

        """
        # instead of counter
        A = A.split()
        A_ctn = {}
        for word in A:
            if word not in A_ctn: A_ctn[word] = 0
            A_ctn[word] += 1
        """

        uncommon = [word for word in A_ctn if A_ctn[word]
                    == 1 and word not in B_ctn]
        for word in B_ctn:
            if B_ctn[word] == 1 and word not in A_ctn:
                uncommon.append(word)

        return uncommon


"""
Runtime: O(A+B+wA+wB)
Space: O(A+B)
where A = length of A, B = length of B, wA = no. of words in A, wB= no. of words in B

Runtime: 28 ms, faster than 68.16% of Python3 online submissions for Uncommon Words from Two Sentences.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Uncommon Words from Two Sentences.
"""
