"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
Difficulty: Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid. Valid means: open brackets are closed
by the same type, and in the correct order.

Examples:
    Input: s = "()"
    Output: true

    Input: s = "()[]{}"
    Output: true

    Input: s = "(]"
    Output: false

Constraints:
    - 1 <= s.length <= 10^4
    - s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # Hint: Use a stack. Push opening brackets. For closing brackets,
        # check if the top of the stack is the matching opening bracket.
        # Map: ')' -> '(', ']' -> '[', '}' -> '{'.
        pass
