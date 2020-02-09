class TrieNode:

    def __init__(self, val):
        self.val = val
        self.next = {}
        self.end = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for char in word:
            if char not in cur.next:
                cur.next[char] = TrieNode(char)
            cur = cur.next[char]

        cur.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for char in word:
            if char not in cur.next:
                return False
            cur = cur.next[char]

        return cur.end == True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for char in prefix:
            if char not in cur.next:
                return False
            cur = cur.next[char]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

"""
Runtime: O(w*l)
Space: O(longest_word_length * 26)
w = no of words
l = average length of a word

Runtime: 176 ms, faster than 68.34% of Python3 online submissions for Implement Trie (Prefix Tree).
Memory Usage: 30.3 MB, less than 18.52% of Python3 online submissions for Implement Trie (Prefix Tree).
"""
