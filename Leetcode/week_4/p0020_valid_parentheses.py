class Solution:
    def isValid(self, s: str) -> bool:
        return self.stack_soln(s)

    def stack_soln(self, s: str) -> bool:
        # soln with stacks
        stack = []
        for char in s:
            if stack:
                if char in '([{':
                    stack.append(char)
                else:
                    end = stack[-1]
                    if char == '}':
                        if end != '{':
                            return False
                    elif char == ')':
                        if end != '(':
                            return False
                    elif char == ']':
                        if end != '[':
                            return False
                    stack.pop()
            else:
                if char in ')}]':
                    return False
                stack.append(char)

        return stack == []


"""
Runtime: O(s)
Space: O(s)

Runtime: 28 ms, faster than 71.67% of Python3 online submissions for Valid Parentheses.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.
"""
