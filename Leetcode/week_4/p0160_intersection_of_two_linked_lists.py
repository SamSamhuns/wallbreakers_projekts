class Solution():
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        Two pointer solution
        """
        a, b = headA, headB
        if a is None or b is None:
            return None

        la, lb = 1, 1
        while a != b:
            a = a.next
            b = b.next
            if a is None and b is None:
                return None
            if a is None:
                if la:
                    a = headB
                    la = 0
                else:
                    a = headA
                    la = 1
            if b is None:
                if lb:
                    b = headA
                    lb = 0
                else:
                    b = headB
                    lb = 1

        return a


"""
Runtime: O(N)
Space: O(1)

Runtime: 192 ms, faster than 79.07% of Python online submissions for Intersection of Two Linked Lists.
Memory Usage: 41.9 MB, less than 12.00% of Python online submissions for Intersection of Two Linked Lists.
"""
