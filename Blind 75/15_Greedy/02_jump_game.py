"""
55. Jump Game
https://leetcode.com/problems/jump-game/
Difficulty: Medium

Given an array nums where nums[i] is the max jump length from position i,
determine if you can reach the last index starting from the first index.

Examples:
    Input: nums = [2,3,1,1,4]
    Output: true

    Input: nums = [3,2,1,0,4]
    Output: false

Constraints:
    - 1 <= nums.length <= 10^4
    - 0 <= nums[i] <= 10^5
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Hint: Greedy. Track the farthest index reachable. Iterate through
        # the array: if current index > farthest, return False.
        # Update farthest = max(farthest, i + nums[i]).
        pass
