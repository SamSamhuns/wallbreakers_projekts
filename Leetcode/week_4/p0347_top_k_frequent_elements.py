import heapq as hq
from typing import List
from collections import defaultdict


class Heap:

    def __init__(self, arr):
        self.arr = []
        for elem in arr:
            self.arr.append(elem)
        Heap.heapify(self.arr)

    @staticmethod
    def heapify(arr):
        for i in range(len(arr) // 2, -1, -1):
            Heap._sift_down(arr, i)

    @staticmethod
    def _sift_down(arr, i):
        l, r = 2 * i + 1, 2 * i + 2
        smallest = i
        if l < len(arr) and arr[smallest][0] > arr[l][0]:
            smallest = l
        if r < len(arr) and arr[smallest][0] > arr[r][0]:
            smallest = r
        if i != smallest:
            arr[smallest], arr[i] = arr[i], arr[smallest]
            Heap._sift_down(arr, smallest)

    @staticmethod
    def _sift_up(arr, i):
        parent = (i - 1) // 2
        if parent >= 0 and arr[parent][0] > arr[i][0]:
            arr[parent], arr[i] = arr[i], arr[parent]
            Heap._sift_up(arr, parent)

    def pop(self):
        if len(self.arr) == 0:
            return
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        smallest = self.arr.pop()
        Heap._sift_down(self.arr, 0)

        return smallest[1]


class Solution:
    def topKFrequentCustom(self, nums: List[int], k: int) -> List[int]:
        """
        Runtime: O(Nlogk)
        Space: O(n)
        """
        count_dict = defaultdict(int)
        for n in nums:
            count_dict[n] -= 1

        hq = Heap([[val, key] for key, val in count_dict.items()])
        top_k = [0] * k

        for i in range(k):
            top_k[i] = hq.pop()

        return top_k

    def topKFrequentHeapq(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        Solution using hashmap and a priority queue or heapq
        """
        countMap = {}
        for n in nums:
            countMap[n] = countMap.get(n, 0) + 1

        countKey = [[-countMap[key], key] for key in countMap]
        hq.heapify(countKey)

        return [hq.heappop(countKey)[1] for i in range(k)]


"""
Runtime: O(Nlogk)
Space: O(N)

Runtime: 116 ms, faster than 26.91% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 17.4 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.
"""
