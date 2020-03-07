from typing import List
from collections import deque, defaultdict


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        Bipartite graph.
        Start from one node and branch out,
        adjacent nodes should be assigned to alternating sets (0 or 1)
        otherwise graph cannot be bipartite

        Groups assigned is 1 or 0
        """
        return self.bfs(graph)

    def dfs(self, graph: List[List[int]]) -> bool:
        self.node_group = defaultdict(int)
        self.seen = set()

        adj_map = defaultdict(set)
        for i, connections in enumerate(graph):
            for n in connections:
                adj_map[i].add(n)

        def _dfs_assign(cnode, is_invalid, last_group):
            if is_invalid[0]:
                return
            new_group = last_group ^ 1  # switch groups
            self.node_group[cnode] = new_group
            self.seen.add(cnode)

            for n in adj_map[cnode]:
                # invalid grouping discovered
                if n in self.node_group and self.node_group[n] == new_group:
                    is_invalid[0] = True
                    return
                if n not in self.seen:
                    _dfs_assign(n, is_invalid, new_group)

        for n in range(len(graph)):
            is_invalid = [False]
            if n not in self.seen:
                # opposite of group 1 or group 0 is assigned first
                _dfs_assign(n, is_invalid, 1)
            if is_invalid[0]:
                return False

        return True

    def bfs(self, graph: List[List[int]]) -> bool:
        self.node_group = defaultdict(int)
        self.seen = set()

        adj_map = defaultdict(set)
        for i, connections in enumerate(graph):
            for n in connections:
                adj_map[i].add(n)

        cgroup = 1
        for n in range(len(graph)):
            if n in self.seen:
                continue

            queue = deque([n])
            self.seen.add(n)
            while queue:
                for i in range(len(queue)):
                    cnode = queue.popleft()
                    self.node_group[cnode] = cgroup
                    for node in adj_map[cnode]:
                        # invalid grouping discovered
                        if node in self.node_group and self.node_group[node] == cgroup:
                            return False
                        if node not in self.seen:
                            self.seen.add(node)
                            queue.append(node)
                # level change
                cgroup ^= 1  # switch group
        return True


"""
Runtime: O(V)
Space: O(EV)

Runtime: 192 ms, faster than 41.40% of Python3 online submissions for Is Graph Bipartite?.
Memory Usage: 13.7 MB, less than 27.27% of Python3 online submissions for Is Graph Bipartite?.
"""
