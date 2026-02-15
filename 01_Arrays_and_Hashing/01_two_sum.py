"""
1. Two Sum
https://leetcode.com/problems/two-sum/
Difficulty: Easy

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Examples:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]

    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Constraints:
    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - Only one valid answer exists.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hint: Use a hash map to store each number's index as you iterate.
        # For each number, check if (target - number) already exists in the map.
        pass
