""" 32. Longest Valid Parentheses
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed)
parentheses substring.
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        bit_memory = 0
        count = []
        for i, c in enumerate(s):
            if c == '(':
                count.append(i)
            elif len(count) > 0:
                bit_memory |= 1 << i
                bit_memory |= 1 << count.pop()
        return max(len(x) for x in format(bit_memory, 'b').split('0'))


# test solition
solution = Solution()
s = ")()())"
print(solution.longestValidParentheses(s))
