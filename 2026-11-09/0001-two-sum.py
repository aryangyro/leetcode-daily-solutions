# LeetCode 1. Two Sum
# Difficulty: Easy | 2026-11-09
# https://leetcode.com/problems/two-sum/
#
# Idea: one pass with a hash map. For each number, check if its
# complement (target - num) was seen before; if so, those two
# indices are the answer. Otherwise store the number and its index.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i
