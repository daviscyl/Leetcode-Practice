""" #44 Wild Card Matching
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character. '*' Matches any sequence of characters (including the empty sequence). The
matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z. p could be empty and contains only lowercase letters
a-z, and characters like ? or *.
"""

from collections import defaultdict


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        nexts = 1
        end_bit = 1 << len(s)
        d = defaultdict(int)
        for i, c in enumerate(s):
            d[c] |= 1 << i
        for c in p:
            if c == '*':
                nexts = (end_bit << 1) - (nexts & -nexts)
            elif c == '?':
                nexts <<= 1
            else:
                nexts = (nexts & d[c]) << 1
            if nexts == 0:
                return False
        return nexts & end_bit != 0


# test solition
solution = Solution()
s = "acdcb"
p = "a*c?b"
print(solution.isMatch(s, p))
