from typing import List
from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        domain_visits = defaultdict(int)

        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            dots_idx = [i for i, char in enumerate(domain) if char == '.']

            domain_visits[domain] += int(count)
            for idx in dots_idx:
                domain_visits[domain[idx + 1:]] += int(count)

        return [' '.join([str(domain_visits[dom]), dom]) for dom in domain_visits]


"""
Runtime: O(4N) ~ O(N) runtime
Space: O(N)

Runtime: 52 ms, faster than 73.52% of Python3 online submissions for Subdomain Visit Count.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Subdomain Visit Count.
"""
