class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = even_head
        return head


"""
Runtime: O(N)
Space: O(1)

Runtime: 32 ms, faster than 98.43% of Python3 online submissions for Odd Even Linked List.
Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for Odd Even Linked List.
"""
