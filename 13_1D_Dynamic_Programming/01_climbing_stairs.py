"""
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/
Difficulty: Easy

You are climbing a staircase. It takes n steps to reach the top.
Each time you can climb 1 or 2 steps. How many distinct ways can you climb?

Examples:
    Input: n = 2
    Output: 2  (1+1 or 2)

    Input: n = 3
    Output: 3  (1+1+1, 1+2, 2+1)

Constraints:
    - 1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # Hint: dp[i] = dp[i-1] + dp[i-2], same as Fibonacci.
        # Base cases: dp[1] = 1, dp[2] = 2. Only need two variables.
        pass
