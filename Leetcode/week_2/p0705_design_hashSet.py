class HashSetNode:
    __slots__ = ['val', 'next']

    def __init__(self, val):
        self.val = val
        self.next = None


class MyHashSet:
    """
    Chained hashing solution to limit memory usage

    Runtime: 188 ms, faster than 67.69% of Python3 online submissions for Design HashSet.
    Memory Usage: 17.2 MB, less than 53.85% of Python3 online submissions for Design HashSet.
    """

    __slots__ = ['size', 'hset_arr']

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.hset_arr = [None] * self.size

    def add(self, key: int) -> None:
        idx = key % self.size  # reduces to size of hset_arr

        if self.contains(key):  # key already exists in hashset
            return

        if self.hset_arr[idx] == None:
            self.hset_arr[idx] = HashSetNode(key)
            return

        cur = self.hset_arr[idx]
        while cur.next:
            cur = cur.next
        cur.next = HashSetNode(key)

    def remove(self, key: int) -> None:
        idx = key % self.size  # reduces to size of hset_arr
        if self.hset_arr[idx] == None:
            return
        prev, cur = None, self.hset_arr[idx]

        while cur:
            if cur.val == key:
                if prev is None:
                    self.hset_arr[idx] = cur.next
                else:
                    prev.next = cur.next
                return
            prev = cur
            cur = cur.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx = key % self.size  # reduces to size of hset_arr
        if self.hset_arr[idx] == None:
            return False

        cur = self.hset_arr[idx]
        while cur:
            if cur.val == key:
                return True
            cur = cur.next
        return False


class MyHashSetArr:
    """
    Giant list solution
    Takes a huge chunk of memory

    Runtime: 300 ms, faster than 31.95% of Python3 online submissions for Design HashSet.
    Memory Usage: 40.1 MB, less than 7.69% of Python3 online submissions for Design HashSet.
    """

    __slots__ = ['size', 'hset_arr']

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hset_arr = [None] * 1000000

    def add(self, key: int) -> None:
        self.hset_arr[key] = 1

    def remove(self, key: int) -> None:
        self.hset_arr[key] = None

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.hset_arr[key] != None

"""
Chained hashing solution

Runtime: amortized average case O(1), Worst Case O(N)
Space: O(self.max_size)

Runtime: 196 ms, faster than 63.90% of Python3 online submissions for Design HashSet.
Memory Usage: 17.2 MB, less than 53.85% of Python3 online submissions for Design HashSet.
"""
