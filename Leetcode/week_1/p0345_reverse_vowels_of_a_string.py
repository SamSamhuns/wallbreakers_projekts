class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        vidx = []

        for i, char in enumerate(s):
            if char in vowels:
                vidx.append(i)

        ls = list(s)
        vlen = len(vidx)
        for i in range(vlen // 2):
            ls[vidx[i]], ls[vidx[vlen - 1 - i]
                            ] = ls[vidx[vlen - 1 - i]], ls[vidx[i]]

        return ''.join(ls)


"""
Runtime: O(s+v) string length + vowel length
Space: O(s+v) vowel length

Runtime: 44 ms, faster than 92.85% of Python3 online submissions for Reverse Vowels of a String.
Memory Usage: 15.1 MB, less than 6.67% of Python3 online submissions for Reverse Vowels of a String.
"""
