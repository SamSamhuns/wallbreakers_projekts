from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """
        Runtime: O(B * 2N) ~ O(BN) N = length of formula, B = no of bracketed expressions
        Space: O(N)
        """

        def parse_formula(formula: str):  # O(n) operation
            """
            IMPORTANT USE REGEX
            """
            form = []
            temp_elem = []
            temp_digit = 0
            for i, char in enumerate(formula):
                if char.isalpha():
                    if char.isupper() and temp_elem != []:
                        form.append(''.join(temp_elem))
                        temp_elem = []
                    temp_elem.append(char)
                else:
                    if temp_elem != []:
                        form.append(''.join(temp_elem))
                    temp_elem = []

                if char.isdigit():
                    temp_digit = temp_digit * 10 + int(char)
                else:
                    if temp_digit != 0:
                        form.append(str(temp_digit))
                    temp_digit = 0

                if char in '()':
                    form.append(char)

            if temp_elem != []:
                form.append(''.join(temp_elem))
            if temp_digit != 0:
                form.append(str(temp_digit))

            return form

        formula = parse_formula(formula)
        counter = defaultdict(int)

        mult_stack = []        # multiplier stack
        last_elem = ""         # holds elem name
        last_mult = (1, -1)     # holds last multiplier value and idx

        # K4(OMg(SO3)12)2
        # ["K", "4", "(", "O", "Mg", "(", "S", "O", "3", ")", "12", ")", "2"]
        for i, item in enumerate(reversed(formula)):
            if item == ')':
                mult_stack.append(last_mult)
                last_mult = (1, -1)  # reset last mult
            elif item == '(':
                mult_stack.pop()
            elif item.isalpha():
                stack_mult = 1
                for mult in mult_stack:
                    stack_mult *= mult[0]

                last_mult = last_mult if last_mult[1] == i - 1 else (1, -1)
                counter[item] += last_mult[0] * stack_mult
                last_mult = (1, -1)
            elif item.isdigit():
                last_mult = (int(item), i)

        sorted_counter = sorted(
            [key + str(counter[key]) if counter[key] > 1 else key for key in counter])
        return ''.join(sorted_counter)


"""
Runtime: O(B * 2N) ~ O(BN) N = length of formula, B = no of bracketed expressions
Space: O(N)

Runtime: 32 ms, faster than 48.39% of Python3 online submissions for Number of Atoms.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Number of Atoms.
"""
