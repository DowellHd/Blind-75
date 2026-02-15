"""
268. Missing Number
https://leetcode.com/problems/missing-number/
Difficulty: Easy

Given an array nums containing n distinct numbers in the range [0, n],
return the one number that is missing.

Examples:
    Input: nums = [3,0,1]
    Output: 2

    Input: nums = [0,1]
    Output: 2

    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8

Constraints:
    - n == nums.length
    - 0 <= nums[i] <= n
    - All numbers are unique.
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Hint: XOR all indices (0 to n) and all values. Duplicates cancel out,
        # leaving only the missing number. Alternative: sum(0..n) - sum(nums).
        pass
