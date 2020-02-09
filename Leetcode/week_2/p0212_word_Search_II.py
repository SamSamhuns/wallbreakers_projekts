from typing import List
from collections import defaultdict


class TrieNode:

    __slots__ = ['idx', 'val', 'next', 'end']

    def __init__(self, val):
        self.idx = -1
        self.val = val
        self.next = {}
        self.end = False


class Trie:

    __slots__ = ['root', 'found_words']

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        cur = self.root
        idx = 0
        for char in word:
            if char not in cur.next:
                cur.next[char] = TrieNode(char)
                cur.next[char].idx = idx
            cur = cur.next[char]
            idx += 1
        cur.end = True

    def find_words_in_board(self, board):
        cur = self.root
        self.found_words = []

        def dfs_backtrack(board_coord, cur, path, seen):
            if cur.end:
                cur.end = False  # prevent double addition of words
                self.found_words.append(''.join(path))
            if cur.next == {}:
                return

            x, y = board_coord
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[nx]):
                    if (nx, ny) not in seen:
                        seen.add((nx, ny))
                        char = board[nx][ny]
                        if char in cur.next:
                            dfs_backtrack(
                                (nx, ny), cur.next[char], path + [char], seen)
                        seen.remove((nx, ny))  # backtrack

        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if char in cur.next:
                    dfs_backtrack((i, j), cur.next[char], [
                                  char], set([(i, j)]))

        return self.found_words


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        return self.trie_backtrack(board, words)

    def trie_backtrack(self, board: List[List[str]], words: List[str]) -> List[str]:
        words_trie = Trie()
        _ = [words_trie.insert(word) for word in words]
        return words_trie.find_words_in_board(board)

    def dfs_backtrack(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Brute Force Solution
        TLE Time Limit Exceeded

        Runtime: O(m * n * w * l)
        Space: O(mn + wl)
        m = no of rows, n = no of cols
        w = no of words, l = average length of a word
        """
        self.found_words = []

        trie_next = defaultdict(list)  # stores letter and pos
        for i, row in enumerate(board):
            for j, letter in enumerate(row):
                trie_next[letter].append((i, j))

        def dfs_backtrack(board_idx, word_idx, word, seen):
            if self.found:
                return
            if word_idx == len(word):
                self.found = True
                self.found_words.append(word)
                return

            x, y = board_idx
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[nx]):
                    if board[nx][ny] == word[word_idx] and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        dfs_backtrack((nx, ny), word_idx + 1, word, seen)
                        seen.remove((nx, ny))  # backtrack step

        for word in words:
            for start in trie_next[word[0]]:  # by 1st char
                self.found = False
                dfs_backtrack(start, 1, word, set([start]))
                if self.found:
                    break  # prevent repetitive work

        return self.found_words


"""
For trie_backtrack solution 
Runtime: O max(m * n * w * l, w*l)
Space: O(mn + wl)
m = no of rows, n = no of cols
w = no of words, l = average length of a word


Runtime: 416 ms, faster than 34.43% of Python3 online submissions for Word Search II.
Memory Usage: 26.4 MB, less than 100.00% of Python3 online submissions for Word Search II.
"""
