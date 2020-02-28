class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.stack_soln(S, T)

    def stack_soln(self, S: str, T: str) -> bool:
        """
        Solution with stacks
        Runtime: O(S+T) + O(min(S, T))
        Space: O(S+T)
        """
        stack_s = []
        stack_t = []

        for char in S:
            if char == '#':
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(char)

        for char in T:
            if char == '#':
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(char)

        return stack_s == stack_t


"""
Runtime: O(S+T) + O(min(S, T))
Space: O(S+T)

Runtime: 28 ms, faster than 72.50% of Python3 online submissions for Backspace String Compare.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Backspace String Compare.
"""
