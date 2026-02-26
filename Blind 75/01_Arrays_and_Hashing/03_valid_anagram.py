"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/
Difficulty: Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Examples:
    Input: s = "anagram", t = "nagaram"
    Output: true

    Input: s = "rat", t = "car"
    Output: false

Constraints:
    - 1 <= s.length, t.length <= 5 * 10^4
    - s and t consist of lowercase English letters.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Hint: Count character frequencies using a hash map or Counter.
        # Compare the two frequency maps. They must be identical.
        # Two dictionaries to track how many times each character appears
        character_count_s = {}
        character_count_t = {}

        for char in s:
            # .get(char, 0) looks up `char` in the dict.
            # If `char` exists, it returns its current count.
            # If `char` is NOT in the dict yet, it returns the default value 0
            # instead of raising a KeyError.
            # We then add 1 and store the result back, incrementing the count.
            character_count_s[char] = character_count_s.get(char, 0) + 1

        for char in t:
            character_count_t[char] = character_count_t.get(char, 0) + 1

        # Two dicts are equal in Python if they have the same keys and values.
        # If both strings have identical character frequencies, they are anagrams.
        return character_count_s == character_count_t
    
test = Solution()
print(test.isAnagram("anagram", "nagamam"))