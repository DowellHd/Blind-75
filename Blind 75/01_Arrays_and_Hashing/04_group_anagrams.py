"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/
Difficulty: Medium

Given an array of strings strs, group the anagrams together.

Examples:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    Input: strs = [""]
    Output: [[""]]

Constraints:
    - 1 <= strs.length <= 10^4
    - 0 <= strs[i].length <= 100
    - strs[i] consists of lowercase English letters.
"""

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Approach: character count fingerprint
        # Each word is represented as a tuple of 26 counts (one per letter a-z).
        # Anagrams produce identical tuples, so they map to the same bucket.
        # Time: O(n * k)  |  Space: O(n * k)  — where n = # words, k = max word length
        anagram_groups = defaultdict(list) # mapping charCount to List of Anagrams

        for word in strs:
            charcount = [0] * 26  # frequency table for each letter a-z
            for char in word:
                charcount[ord(char) - ord('a')] += 1  # map 'a'->0, 'b'->1, ..., 'z'->25
            anagram_groups[tuple(charcount)].append(word)  # group words with the same fingerprint

        return list(anagram_groups.values())


if __name__ == "__main__":
    s = Solution()

    def check(result, expected):
        result_sorted = sorted([sorted(g) for g in result])
        expected_sorted = sorted([sorted(g) for g in expected])
        status = "PASS" if result_sorted == expected_sorted else "FAIL"
        print(f"[{status}] {result}")

    # Standard case
    check(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]),
          [["eat","tea","ate"], ["tan","nat"], ["bat"]])

    # Single empty string
    check(s.groupAnagrams([""]), [[""]])

    # Multiple empty strings
    check(s.groupAnagrams(["", ""]), [["", ""]])

    # Single character strings
    check(s.groupAnagrams(["a"]), [["a"]])

    # All words are anagrams of each other
    check(s.groupAnagrams(["abc", "bca", "cab"]), [["abc","bca","cab"]])

    # No anagrams (all distinct)
    check(s.groupAnagrams(["abc", "def", "ghi"]), [["abc"], ["def"], ["ghi"]])