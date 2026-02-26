"""
271. Encode and Decode Strings
https://leetcode.com/problems/encode-and-decode-strings/
Difficulty: Medium

Design an algorithm to encode a list of strings to a single string. The
encoded string is then decoded back to the original list of strings.

Examples:
    Input: ["lint","code","love","you"]
    Encoded: "4#lint4#code4#love3#you"

    Input: ["we","say","#","yes"]
    Encoded: "2#we3#say1##3#yes"

Constraints:
    - 0 <= strs.length <= 200
    - 0 <= strs[i].length <= 200
    - strs[i] contains any possible characters out of 256 valid ASCII characters.
"""

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        # Hint: Use length-prefix encoding: for each string, prepend its
        # length followed by a delimiter like '#'. e.g., "4#lint".
        pass

    def decode(self, s: str) -> List[str]:
        # Hint: Read the length up to '#', then extract that many characters.
        pass
