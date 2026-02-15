"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy

Given a string s, return true if it is a palindrome after converting to
lowercase and removing all non-alphanumeric characters.

Examples:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true ("amanaplanacanalpanama")

    Input: s = "race a car"
    Output: false

Constraints:
    - 1 <= s.length <= 2 * 10^5
    - s consists only of printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Hint: Two pointers from both ends. Skip non-alphanumeric characters.
        # Compare lowercase characters moving inward.
        pass
