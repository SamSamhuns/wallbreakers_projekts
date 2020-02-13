def arrayPairSum(nums):
    nums.sort()
    mS = 0
    for i in range(0, len(nums), 2):
        mS += nums[i]

    return mS


"""
Runtime: O(nlogn)
Space: O(1)

Runtime: 312 ms, faster than 25.64% of Python3 online submissions for Array Partition I.
Memory Usage: 15.2 MB, less than 6.06% of Python3 online submissions for Array Partition I.
"""
