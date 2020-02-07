from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        return ['FizzBuzz' if num % 3 == 0 and num % 5 == 0
                else 'Fizz' if num % 3 == 0
                else 'Buzz' if num % 5 == 0
                else str(num) for num in range(1, n + 1)]


"""
Runtime: O(n)
Space: O(n)

Runtime: 36 ms, faster than 94.02% of Python3 online submissions for Fizz Buzz.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Fizz Buzz.
"""
