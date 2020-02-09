from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        morse_code_ls = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                         "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        morse_code_set = set()

        for word in words:
            morse_code_set.add(
                ''.join([morse_code_ls[ord(char) - 97] for char in word]))

        return len(morse_code_set)


"""
Runtime: O(wl) where w = no of words, l = average length of words
Space: O(N)

Runtime: 36 ms, faster than 44.01% of Python3 online submissions for Unique Morse Code Words.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Unique Morse Code Words.
"""
