"""
207. Course Schedule
https://leetcode.com/problems/course-schedule/
Difficulty: Medium

There are numCourses courses (0 to numCourses-1). Given prerequisites pairs
[ai, bi] meaning you must take bi before ai, return true if you can finish
all courses (i.e., no cycles in the dependency graph).

Examples:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true

    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false

Constraints:
    - 1 <= numCourses <= 2000
    - 0 <= prerequisites.length <= 5000
"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Hint: Build adjacency list. DFS cycle detection with 3 states:
        # unvisited, in-progress, completed. If you visit an in-progress
        # node, there's a cycle. Alternative: BFS topological sort (Kahn's).
        pass
