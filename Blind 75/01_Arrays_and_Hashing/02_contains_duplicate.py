"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy

Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.

Examples:
    Input: nums = [1,2,3,1]
    Output: true

    Input: nums = [1,2,3,4]
    Output: false

Constraints:
    - 1 <= nums.length <= 10^5
    - -10^9 <= nums[i] <= 10^9
"""

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Approach: Use a HashSet to detect duplicates in one pass.
        #
        # Steps:
        # 1. Create an empty set to track numbers we've already seen.
        # 2. Iterate through each number in the array.
        # 3. If the number is already in the set, we found a duplicate -> return True.
        # 4. Otherwise, add the number to the set and continue.
        # 5. If we finish the loop without finding a duplicate, return False (implicit).
        #
        # Why a set? Checking membership in a set is O(1) on average,
        # making the overall solution O(n) time and O(n) space.
        #
        # Alternative one-liner: return len(nums) != len(set(nums))
        distinct_nums = set()
        for num in nums:
            if num in distinct_nums:
                return True
            distinct_nums.add(num)
            
nums = [1,2,3,1]
solution = Solution()
print(solution.containsDuplicate(nums))