from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.subsets_backtracking(nums)

    def subsets_backtracking(self, nums: List[int]) -> List[List[int]]:

        self.power_list = []

        def _recurse(max_len, cur_len, index, path):
            if cur_len == max_len:
                self.power_list.append(path)
                return

            for i, n in enumerate(nums[index:], start=index):
                _recurse(max_len, cur_len + 1, i + 1, path + [n])

        for length in range(len(nums) + 1):
            _recurse(length, 0, 0, [])

        return self.power_list

    def subsets_dfs(self, nums: List[int]) -> List[List[int]]:
        temp_arr = [""] * len(nums)
        subsets = []

        def recurse(subsets, nums, temp_arr, index):
            if index == (len(nums)):
                subsets.append([x for x in temp_arr if x != ""])
                return

            temp_arr[index] = ""
            recurse(subsets, nums, [x for x in temp_arr], index + 1)
            temp_arr[index] = nums[index]
            recurse(subsets, nums, [x for x in temp_arr], index + 1)

        recurse(subsets, nums, temp_arr, 0)
        return subsets


"""
Runtime: O(N 2^N)

Runtime: 36 ms, faster than 29.84% of Python3 online submissions for Subsets.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Subsets.
"""
