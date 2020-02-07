class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:

        self.dsu_arr = [i for i in range(len(M))]

        def get_root(node):
            while node != self.dsu_arr[node]:
                # path compression
                self.dsu_arr[node] = self.dsu_arr[self.dsu_arr[node]]
                node = self.dsu_arr[node]
            return node

        for i, row in enumerate(M):
            for j in range(i + 1, len(row)):
                i_root = get_root(i)
                j_root = get_root(j)
                if row[j] == 1 and i_root != j_root:
                    self.dsu_arr[j_root] = i_root

        self.dsu_arr = [get_root(node) for node in self.dsu_arr]
        return len(set(self.dsu_arr))


"""
Runtime: O(n*n) Average Case will be better than O(n^2)
Space: O(n)
where n = no. of nodes

Runtime: 232 ms, faster than 32.46% of Python3 online submissions for Friend Circles.
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Friend Circles.
"""
