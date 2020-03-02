from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.recursive_backtrack_slower(nums)

    def recursive_backtrack_slower(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []

        def recursive_backtrack_generate(start):
            self.permutations.append(nums[::])
            for i in range(start, len(nums)):
                for j in range(i, len(nums)):
                    if i != j:
                        nums[i], nums[j] = nums[j], nums[i]
                        recursive_backtrack_generate(i + 1)
                        nums[i], nums[j] = nums[j], nums[i]

        recursive_backtrack_generate(0)
        return self.permutations

    def recursive_backtrack_faster(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []

        def recursive_backtrack_generate(index):
            if index == len(nums):
                self.permutations.append(nums[::])
                return

            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                recursive_backtrack_generate(index + 1)
                nums[i], nums[index] = nums[index], nums[i]

        recursive_backtrack_generate(0)
        return self.permutations

    def permute_dfs(self, nums: List[int]) -> List[List[int]]:

        permutations = []

        def dfs(nums, permutations, order):
            if not nums:
                permutations.append(order)
                return
            for i, n in enumerate(nums):
                dfs(nums[:i] + nums[i + 1:], permutations, order + [nums[i]])

        dfs(nums, permutations, [])
        return permutations


"""

Runtime: 32 ms, faster than 95.39% of Python3 online submissions for Permutations.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Permutations.
"""
