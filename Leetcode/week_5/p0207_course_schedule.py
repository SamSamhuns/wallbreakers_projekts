from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Classic directed cyclic graph detection problem
        DFS with two sets seen and visiting
        """
        self.seen = set()
        self.visiting = set()
        self.adj = defaultdict(set)

        # create adjacency map
        for end, start in prerequisites:
            self.adj[start].add(end)

        def _has_cycle(cnode, cycle_status):
            if cycle_status[0]:
                return

            self.visiting.add(cnode)
            for next_node in self.adj[cnode]:
                if next_node not in self.seen:
                    if next_node in self.visiting:
                        cycle_status[0] = True
                        return
                    _has_cycle(next_node, cycle_status)
            self.seen.add(cnode)

        for n in range(numCourses):
            if n not in self.seen:
                cycle_status = [False]
                _has_cycle(n, cycle_status)
                if cycle_status[0]:
                    return False
            self.visiting = set()  # reset self.visiting

        return True


"""
Runtime: O(N) N = nodes
Space: O(N^2)

Runtime: 96 ms, faster than 87.63% of Python3 online submissions for Course Schedule.
Memory Usage: 16.5 MB, less than 10.20% of Python3 online submissions for Course Schedule.
"""
