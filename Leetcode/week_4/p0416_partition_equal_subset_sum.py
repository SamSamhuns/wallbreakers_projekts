from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        return self.exhasutive_backtracking(nums)

    def dp_soln(self, nums: List[int]) -> bool:
        """
        Runtime: 2588 ms, faster than 13.09% of Python3 online submissions for Partition Equal Subset Sum.
        Memory Usage: 16.6 MB, less than 9.09% of Python3 online submissions for Partition Equal Subset Sum.

        for arr = [5 3 3 6 1]
        ans = 1 3 5 and 3 6

        Check whether all sums less than or equal to
        sum(arr)/2 is possible
        half = sum(arr)/2 = 9

            Sums(j) 0 1 2 3 4 5 6 7 8 9
        Nums 0      T F F F F F F F F F
     used(i) 1(5)   T F F F F T F F F F
             2(3)   T F F T F T F F T F
             3(3)   T F F T F T T F T F
             4(6)   T F F T F T T F T T
             5(1)   T T F T T T T T T T

        If we don't decide to use a number nums[i] for the sum j,
        we use the bool dp[i-1][j]
        but if we decide to use it, we have an or operation
        with dp[i-1][j-nums[i]]
        """
        n = len(nums)
        max_val = float('-inf')
        nums_sum = 0
        for num in nums:
            nums_sum += num
            max_val = max(max_val, num)

        half = nums_sum // 2
        if nums_sum & 1:
            return False  # odd sum
        if max_val > half:
            return False  # largest num greater than half sum

        dp = [[False] * (half + 1) for _ in range(n + 1)]

        dp[0][0] = True  # sum 0 can be reached with 0 numbers
        for i in range(n):
            # sum 0 can be reached with any numbers by not taking them
            dp[i + 1][0] = True
        for i in range(1, n + 1):  # loop through nums arr
            for j in range(1, half + 1):  # loop through the sum values
                dp[i][j] = dp[i - 1][j]  # assuming num not used
                if j >= nums[i - 1]:    # assume num is used now
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

        return dp[-1][-1]

    def exhasutive_backtracking(self, nums: List[int]) -> bool:
        """
        Runtime: 68 ms, faster than 77.88% of Python3 online submissions for Partition Equal Subset Sum.
        Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Partition Equal Subset Sum.
        """
        tsum = sum(nums)
        if tsum & 1:
            return False
        if max(nums) > tsum // 2:
            return False

        found = [False]
        nums.sort(reverse=True)

        def bk(found, index, csum, hsum):
            if csum == (hsum):
                found[0] = True
            elif csum > (hsum):
                return

            if found[0]:
                return

            for i in range(index, len(nums)):
                csum += nums[i]
                bk(found, i + 1, csum, hsum)
                csum -= nums[i]

        bk(found, 0, 0, tsum // 2)
        return found[0]


"""
Backtracking Solution

Runtime: 68 ms, faster than 77.88% of Python3 online submissions for Partition Equal Subset Sum.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Partition Equal Subset Sum.

2D DP solution
Runtime: 2588 ms, faster than 13.09% of Python3 online submissions for Partition Equal Subset Sum.
Memory Usage: 16.6 MB, less than 9.09% of Python3 online submissions for Partition Equal Subset Sum.
"""
