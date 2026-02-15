"""
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/
Difficulty: Medium

Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence. Must run in O(n) time.

Examples:
    Input: nums = [100,4,200,1,3,2]
    Output: 4  (sequence: [1,2,3,4])

    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9

Constraints:
    - 0 <= nums.length <= 10^5
    - -10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Hint: Put all numbers in a set. For each number where (num - 1) is
        # NOT in the set (it's the start of a sequence), count consecutive
        # numbers upward. Track the max length.
        pass
