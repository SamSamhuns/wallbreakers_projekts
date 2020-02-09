from collections import Counter


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return self.counter_soln(J, S)

    def hset_soln(self, J: str, S: str) -> int:
        J_set = set(J)
        return sum([1 for s in S if s in J_set])

    def counter_soln(self, J: str, S: str) -> int:
        J_set = set(J)
        S_counter = Counter(S)
        return sum([S_counter[s] for s in S_counter if s in J_set])


"""
Runtime: O(J+S)
Space: O(J+S)

Runtime: 28 ms, faster than 71.06% of Python3 online submissions for Jewels and Stones.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Jewels and Stones.
"""
