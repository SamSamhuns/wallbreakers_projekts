from typing import List


class TrieNode:

    def __init__(self, val):
        self.val = val
        self.next = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = TrieNode(None)
        self.max_word = ""

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.next:
                cur.next[c] = TrieNode(c)
            cur = cur.next[c]
        cur.end = True

    def _trie_dfs(self, node, word):
        if node.next == {} or node.end:
            wlen = len(word)
            maxlen = len(self.max_word)
            if wlen >= maxlen:
                str_word = ''.join(word)

                if wlen == maxlen:
                    self.max_word = min(str_word, self.max_word)
                else:
                    self.max_word = str_word

        for val in node.next:
            if node.next[val].end:
                self._trie_dfs(node.next[val], word + [val])

    def find_max(self):
        self._trie_dfs(self.root, [])
        return self.max_word


class Solution:
    def longestWord(self, words: List[str]) -> str:
        return self.trie_soln(words)

    def hset_soln(self, words: List[str]) -> str:
        """
        Runtime: Two pass O(2n) ~ O(n)
        Space: O(n)
        """
        longest = ""
        word_set = set()

        for word in words:
            word_set.add(word)

        for word in words:
            found_sub = True
            for i in range(len(word)):
                if word[:i + 1] not in word_set:
                    found_sub = False
                    break
            if found_sub:
                len_long, len_word = len(longest), len(word)
                if len_long == len_word:
                    longest = min(longest, word)
                else:
                    longest = word if len_word > len_long else longest

        return longest

    def trie_soln(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)

        return trie.find_max()


"""
Hashset Solution
Runtime: Two pass O(2n) ~ O(n)
Space: O(n)
Runtime: 148 ms, faster than 35.71% of Python3 online submissions for Longest Word in Dictionary.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Longest Word in Dictionary.

Runtime: Two pass O(n + len(longestWord)*w)
Space: O(len(longestWord) * 26)
Trie Solution
Runtime: 172 ms, faster than 22.49% of Python3 online submissions for Longest Word in Dictionary.
Memory Usage: 13.8 MB, less than 50.00% of Python3 online submissions for Longest Word in Dictionary.
"""
