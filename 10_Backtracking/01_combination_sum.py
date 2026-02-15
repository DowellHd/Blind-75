"""
39. Combination Sum
https://leetcode.com/problems/combination-sum/
Difficulty: Medium

Given an array of distinct integers candidates and a target integer target,
return all unique combinations where the chosen numbers sum to target.
The same number may be chosen an unlimited number of times.

Examples:
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]

    Input: candidates = [2,3,5], target = 8
    Output: [[2,2,2,2],[2,3,3],[3,5]]

Constraints:
    - 1 <= candidates.length <= 30
    - 2 <= candidates[i] <= 40
    - All elements are distinct.
    - 1 <= target <= 40
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Hint: Backtracking. At each step, try adding each candidate
        # (starting from current index to avoid duplicates). If sum == target,
        # add to results. If sum > target, prune. Recurse with remaining target.
        pass
