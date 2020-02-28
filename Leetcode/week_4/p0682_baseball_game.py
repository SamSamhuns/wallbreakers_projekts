class Solution:
    def calPoints(self, ops: List[str]) -> int:
        return self.single_pass(ops)

    def single_pass(self, ops: List[str]) -> int:
        total_score = 0
        score_stack = []
        for score in ops:
            if score[0] == '-' or score.isdigit():
                score = int(score)
                total_score += score
                score_stack.append(score)
            elif score == '+':
                if score_stack:
                    csum = 0
                    for score in score_stack[-1:-3:-1]:
                        csum += score
                    total_score += csum
                    score_stack.append(csum)
            elif score == 'D':
                if score_stack:
                    total_score += (score_stack[-1] * 2)
                    score_stack.append(score_stack[-1] * 2)
            elif score == 'C':
                if score_stack:
                    total_score -= score_stack[-1]
                    score_stack.pop()

        return total_score

    def double_pass(self, ops: List[str]) -> int:
        pstack = []

        for p in ops:
            if p == 'C':
                pstack.pop()
            elif p == 'D':
                pstack.append(pstack[-1] * 2)
            elif p == '+':
                pstack.append(pstack[-1] + pstack[-2])
            else:
                pstack.append(int(p))

        return sum(pstack)

"""
Runtime: O(N)
Space: O(N)

Runtime: 32 ms, faster than 95.85% of Python3 online submissions for Baseball Game.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Baseball Game.
"""
