class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        Reverse in segments

        """
        dummy = ListNode(None)
        dummy.next = head
        cur = head
        prev = None
        idx = 1
        rev_start = head

        # find the point where reversing begins
        while cur:
            if idx < m:
                rev_start = cur
                cur = cur.next
                idx += 1
            else:
                break

        while cur:
            # reverse nodes
            cur_next = cur.next
            cur.next = prev
            prev = cur
            cur = cur_next
            idx += 1

            # reversing ends
            if idx > n:
                if rev_start.next:  # when start node is not 1
                    rev_next = rev_start.next
                    rev_start.next = prev
                    rev_next.next = cur
                else:  # when start node is 1
                    rev_start.next = cur
                break

        return dummy.next if m > 1 else prev


"""
Runtime: O(N)
Space: O(1)

Runtime: 28 ms, faster than 74.04% of Python3 online submissions for Reverse Linked List II.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Reverse Linked List II.
"""
