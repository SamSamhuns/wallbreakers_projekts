class ListNode:

    __slots__ = ['key', 'val', 'next', 'prev']

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    __slots__ = ['map', 'capacity', 'head', 'tail']

    def __init__(self, capacity: int):
        """
        Hashmap and Doubly LinkedList Solution
        Dummy head and tail
        """
        self.map = {}
        self.capacity = capacity
        self.head = ListNode(None, None)
        self.tail = ListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert(self, node):
        # always inserts immediately after head node
        head_next = self.head.next

        self.head.next = node
        head_next.prev = node

        node.prev = self.head
        node.next = head_next

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def get(self, key: int) -> int:
        if key in self.map:
            cnode = self.map[key]
            self._remove(cnode)
            self._insert(cnode)
            return cnode.val
        return -1

    def put(self, key: int, value: int) -> None:
        cnode = ListNode(key, value)
        if key in self.map:
            cnode = self.map[key]
            self._remove(cnode)
            cnode.val = value

        self.map[key] = cnode
        self._insert(cnode)
        if len(self.map) > self.capacity:
            node_to_remove = self.tail.prev
            self._remove(node_to_remove)
            del self.map[node_to_remove.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


"""
Runtime: O(n)
Space: O(n)

Runtime: 212 ms, faster than 60.45% of Python3 online submissions for LRU Cache.
Memory Usage: 21.9 MB, less than 33.33% of Python3 online submissions for LRU Cache.
"""
