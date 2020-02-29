class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        Can only use append, pop, stack[-1] operations
        """
        self.queue = []
        self.size = 0
        self.front = None

    def push(self, x: int) -> None:
        """
        Enqueue
        Push element x to the back of queue.
        """
        self.queue.append(x)
        if self.size == 0:
            self.front = x
        self.size += 1

    def pop(self) -> int:
        """
        O(N) operation
        Two stacks solution
        Dequeue
        Removes the element from in front of queue and returns that element.
        """
        if self.size == 0:
            return None

        to_remove = self.front
        temp_stack = []
        while self.queue[-1] != to_remove:
            temp_stack.append(self.queue.pop())

        if temp_stack == []:
            self.front = self.queue.pop()
        else:
            self.front = temp_stack[-1]
            self.queue.pop()
        while temp_stack:
            self.queue.append(temp_stack.pop())

        self.size -= 1
        return to_remove

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.size == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

"""
Runtime: O(N) for pop, O(1) for push, peek, empty operations 
Space: O(N)

Runtime: 24 ms, faster than 83.23% of Python3 online submissions for Implement Queue using Stacks.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Implement Queue using Stacks.
"""
