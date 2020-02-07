class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == "":
            return True

        if word[0].isupper():
            ucount = 0
            for char in word:
                if char.isupper():
                    ucount += 1
                else:
                    if ucount > 1:
                        return False
            if ucount == 1:
                return True
            return ucount == len(word)

        for char in word:
            if char.isupper():
                return False
        return True


"""
Runtime: O(N)
Space: O(1)

Runtime: 28 ms, faster than 72.64% of Python3 online submissions for Detect Capital.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Detect Capital.
"""
