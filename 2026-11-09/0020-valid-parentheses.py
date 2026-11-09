# LeetCode 20. Valid Parentheses
# Difficulty: Easy | 2026-11-09
# https://leetcode.com/problems/valid-parentheses/
#
# Idea: push opening brackets on a stack. On a closing bracket, the
# top of the stack must be the matching opener, otherwise the string
# is invalid. At the end the stack must be empty.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack
