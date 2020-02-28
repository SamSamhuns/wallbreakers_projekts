class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.iterative_reverse(head)

    def iterative_reverse(self, head: ListNode) -> ListNode:
        cur = head
        prev = None

        while cur:
            cur_next = cur.next
            cur.next = prev
            prev = cur
            cur = cur_next

        return prev

    def recursive_reverse(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        return_node = self.recursive_reverse(head.next)
        head.next.next = head
        head.next = None

        return return_node


"""
Runtime: O(N)
Space: O(1)

Runtime: 32 ms, faster than 81.63% of Python3 online submissions for Reverse Linked List.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Reverse Linked List.
"""
