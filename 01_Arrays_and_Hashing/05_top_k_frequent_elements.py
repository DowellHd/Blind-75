"""
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/
Difficulty: Medium

Given an integer array nums and an integer k, return the k most frequent elements.

Examples:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

    Input: nums = [1], k = 1
    Output: [1]

Constraints:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4
    - k is in the range [1, number of unique elements].
    - Answer is guaranteed to be unique.
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hint: Count frequencies with a hash map, then use bucket sort where
        # index = frequency (O(n)), or use a min-heap of size k (O(n log k)).
        pass
