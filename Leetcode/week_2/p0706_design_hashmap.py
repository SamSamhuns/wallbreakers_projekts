class HashMapNode:

    __slots__ = ['key', 'val', 'next']

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    __slots__ = ['size', 'hmap_arr']

    def __init__(self):
        """
        Initialize your data structure here.
        Chained Hashing solution
        """
        self.size = 1000
        self.hmap_arr = [None] * self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.size

        if self.hmap_arr[idx] == None:
            self.hmap_arr[idx] = HashMapNode(key, value)
            return

        cur = self.hmap_arr[idx]
        while cur.next:
            if cur.key == key:
                cur.val = value
                return
            cur = cur.next

        if cur.key == key:
            cur.val = value
            return
        else:
            cur.next = HashMapNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % self.size
        if self.hmap_arr[idx] == None:
            return -1

        cur = self.hmap_arr[idx]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % self.size
        if self.hmap_arr[idx] == None:
            return

        prev = None
        cur = self.hmap_arr[idx]
        while cur:
            if cur.key == key:
                if prev is None:
                    self.hmap_arr[idx] = cur.next
                else:
                    prev.next = cur.next  # remove node
                return

            prev = cur
            cur = cur.next


"""
Chained hashing solution

Runtime: amortized average case O(1), Worst Case O(N)
Space: O(self.max_size)

Runtime: 212 ms, faster than 84.78% of Python3 online submissions for Design HashMap.
Memory Usage: 15.5 MB, less than 100.00% of Python3 online submissions for Design HashMap.
"""
