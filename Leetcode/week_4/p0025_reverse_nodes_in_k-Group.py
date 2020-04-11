# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k <= 1:
            return head

        dummy = jump = ListNode(None)
        dummy.next = left = right = head

        while True:
            count = 0

            while right and count < k:
                right = right.next
                count += 1

            # standard reversing of nodes
            if count == k:
                cur, prev = left, right

                for _ in range(k):
                    temp = cur.next
                    cur.next = prev
                    prev = cur
                    cur = temp
                jump.next = prev  # connect the last node of the previous reversed k-group to the head of the current reversed k-group
                jump = left  # prepare for connecting to the next to-be-reversed k-group
                left = right
            else:
                return dummy.next

"""
Runtime: 52 ms, faster than 45.64% of Python3 online submissions for Reverse Nodes in k-Group.
Memory Usage: 14.9 MB.
"""
