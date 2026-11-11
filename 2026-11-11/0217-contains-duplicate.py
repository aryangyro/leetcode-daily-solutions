# 217. Contains Duplicate (Easy)
# Idea: a set drops duplicates, so if its size is smaller than the list,
# some value appeared twice.
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)
