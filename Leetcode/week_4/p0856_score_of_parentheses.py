class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        return self.depth_score_stack_soln(S)

    def depth_score_stack_soln(self, S: str) -> int:
        val_stack = [0]  # initially at outside depth score is 0

        for parenthesis in S:
            if parenthesis == '(':
                val_stack.append(0)  # go a level deep
            else:
                popped = val_stack.pop()
                val_stack[-1] += max(2 * popped, 1)

        return val_stack[-1]


"""
Runtime: O(n)
Space: O(n)

Runtime: 24 ms, faster than 83.71% of Python3 online submissions for Score of Parentheses.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Score of Parentheses.
"""
