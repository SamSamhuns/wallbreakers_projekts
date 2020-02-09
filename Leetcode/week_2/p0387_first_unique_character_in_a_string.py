class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_list = []
        char_map = {}

        for i, char in enumerate(s):
            if char in char_map:
                char_map[char] = -1
            else:
                char_map[char] = i
                char_list.append(char)

        min_index = -1
        for char in char_list:
            if char_map[char] != -1:
                # guaranteed to be the min index
                min_index = char_map[char]
                break

        return min_index


"""
Runtime O(2s) ~ O(s)
Space O(s + uniq(s))

Runtime: 112 ms, faster than 61.31% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for First Unique Character in a String.
"""
