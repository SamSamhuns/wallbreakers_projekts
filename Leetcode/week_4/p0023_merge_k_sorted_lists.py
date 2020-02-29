from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Heap:

    __slots__ = ['arr']

    def __init__(self, arr):
        self.arr = arr
        Heap.heapify(self.arr)

    def __repr__(self):
        head_vals = [str(node.val) if node else 'None' for node in self.arr]
        return ' '.join(head_vals)

    @staticmethod
    def heapify(arr):  # O(n)
        for i in range(len(arr) // 2, -1, -1):
            Heap._sift_down(arr, i)

    @staticmethod
    def _sift_down(arr, i):  # O(logn)
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < len(arr) and arr[left].val < arr[smallest].val:
            smallest = left
        if right < len(arr) and arr[right].val < arr[smallest].val:
            smallest = right
        if i != smallest:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            Heap._sift_down(arr, smallest)

    @staticmethod
    def _sift_up(arr, i):  # O(logn)
        parent = (i - 1) // 2
        if parent >= 0 and arr[parent].val > arr[i].val:
            arr[parent], arr[i] = arr[i], arr[parent]
            Heap._sift_up(arr, parent)

    def pop(self):
        rtn = self.arr[0].val
        self.arr[0] = self.arr[0].next
        if self.arr[0] is None:
            self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
            self.arr.pop()

        Heap._sift_down(self.arr, 0)
        return rtn


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        k = no of linked list
        N = no of nodes
        Time Complexity O(Nlogk)
        Space Complexity O(n) + O(k)
        """
        clean_list = [
            node for node in lists if node is not None]  # sanitize list

        hq = Heap(clean_list)
        dummy = ListNode(None)
        cur = ListNode(None)
        dummy.next = cur

        while hq.arr:
            cur.next = ListNode(hq.pop())
            cur = cur.next
        return dummy.next.next


"""
Runtime: O(Nlogk)
Space: O(n) + O(k)

Runtime: 200 ms, faster than 21.48% of Python3 online submissions for Merge k Sorted Lists.
Memory Usage: 16.9 MB, less than 33.33% of Python3 online submissions for Merge k Sorted Lists.
"""
