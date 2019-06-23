""" #44 Wild Card Matching
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character. '*' Matches any sequence of characters (including the empty sequence). The
matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z. p could be empty and contains only lowercase letters
a-z, and characters like ? or *.
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return None


# test solition
solution = Solution()
s = "acdcb"
p = "a*c?b"
print(solution.isMatch(s, p))
