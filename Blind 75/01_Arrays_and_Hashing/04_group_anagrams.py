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
        # Hint: Use sorted(word) as the key in a hash map. All anagrams
        # produce the same sorted string, so they group into the same bucket.
            anagram_groups = defaultdict(list)
            for word in strs:
                # Sort the characters in the word to get the anagram key
                sorted_word = ''.join(sorted(word))
                # Append the original word to the list corresponding to the sorted key
                anagram_groups[sorted_word].append(word)
                
            return list(anagram_groups.values())