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
            
            for str in strs:
                count = [0] * 26  # Count of each character (a-z)
                for char in str:
                    count[ord(char) - ord('a')] += 1 # Increment count for this character
                anagram_groups[tuple(count)].append(str) # Use the count tuple as the key
            return list(anagram_groups.values())
            
            # for str in strs:
            #     # Sort the characters in the word to get the anagram key
            #     sorted_word = ''.join(sorted(word))
            #     # Append the original word to the list corresponding to the sorted key
            #     anagram_groups[sorted_word].append(word)

            # return list(anagram_groups.values())


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