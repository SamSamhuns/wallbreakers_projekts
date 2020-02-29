from typing import List
from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        Can only use enqueue(deque.append) and dequeue(deque.popleft)
        and peek left (stack[0]) operations
        """
        self.stack = deque([])
        self.top_elem = None
        self.len = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)
        self.top_elem = x
        self.len += 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        O(N) operation
        """
        if self.len == 0:
            return None

        current_head = self.stack[0]  # queue peek operation
        to_remove = self.top_elem
        prev = None
        if current_head == to_remove:
            self.stack.popleft()

        while current_head != to_remove:
            if current_head == to_remove:
                self.stack.popleft()
                break
            prev = current_head
            self.stack.append(self.stack.popleft())
            current_head = self.stack[0]

        self.top_elem = prev  # keeps track of stack top
        self.len -= 1
        return to_remove

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.top_elem

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.len == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

"""
Runtime: O(N) for pop(), O(1) for push(), top(), empty()
Space: O(N)

Runtime: 16 ms, faster than 99.48% of Python3 online submissions for Implement Stack using Queues.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Implement Stack using Queues.
"""
