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

if __name__ == "__main__":
    class Solution:
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            # Step 1: Count how many times each number appears.
            # e.g. [1,1,1,2,2,3] → {1:3, 2:2, 3:1}
            count = {}
            # Step 2: Create buckets where index = frequency.
            # freq[i] holds all numbers that appear exactly i times.
            # The max possible frequency is len(nums), so we need len(nums)+1 buckets.
            freq = [[] for i in range(len(nums) + 1)]

            for num in nums:
                count[num] = 1 + count.get(num, 0)
            # Place each number into the bucket matching its frequency.
            # e.g. {1:3, 2:2, 3:1} → freq[3]=[1], freq[2]=[2], freq[1]=[3]
            # c = count of occurrences, num = the number itself
            for num, c in count.items():
                freq[c].append(num)

            res = []
            # Step 3: Iterate buckets from highest frequency down to 1.
            # Collect numbers until we have k results.
            for i in range(len(freq) - 1, 0, -1):
                for num in freq[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
    print(Solution().topKFrequent([1,1,1,2,2,3], 2))
    