from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        return self.findOrder_dfs_topological_sort(numCourses, prerequisites)

    def findOrder_dfs_topological_sort(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Directed graph Topological sorting and
        cycle detection with a seen and visiting set
        """
        self.seen, self.visiting = set(), set()
        self.ts_stack = []

        # create adjacency map
        self.adj_map = defaultdict(set)
        for end, start in prerequisites:
            self.adj_map[start].add(end)

        def _dfs_topological_sort(cnode, has_cycle):
            if has_cycle[0]:
                return

            self.visiting.add(cnode)
            for next_node in self.adj_map[cnode]:
                if next_node not in self.seen:
                    if next_node in self.visiting:
                        has_cycle[0] = True
                        return
                    _dfs_topological_sort(next_node, has_cycle)

            self.ts_stack.append(cnode)
            self.seen.add(cnode)
            self.visiting.remove(cnode)

        for n in range(numCourses):
            has_cycle = [False]
            if n not in self.seen:
                self.visiting = set()
                _dfs_topological_sort(n, has_cycle)
                if has_cycle[0]:  # cycle detected impossible to finish courses
                    return []

        self.ts_stack.reverse()
        return self.ts_stack


"""
DFS with Topological sorting
Runtime: O(V)
Space: O(EV)

Runtime: 104 ms, faster than 65.00% of Python3 online submissions for Course Schedule II.
Memory Usage: 16.5 MB, less than 21.43% of Python3 online submissions for Course Schedule II.
"""
