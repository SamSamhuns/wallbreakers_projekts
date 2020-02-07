class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([word[::-1] for word in s.split()])


"""
Runtime: O(4N) ~ O(N)
Space: O(N)

Runtime: 28 ms, faster than 86.92% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 13.2 MB, less than 96.15% of Python3 online submissions for Reverse Words in a String III.
"""
