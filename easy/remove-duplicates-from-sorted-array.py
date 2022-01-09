# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that 
# each unique element appears only once. The relative order of the elements should be kept the same.

from typing import List
import math

def sorter(a):
    if a == '_':
        return None
    return a

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dict = {}
        for idx, val in enumerate(nums):
            if val in dict:
                nums[idx] = '_'
            dict[val] = True
        nums.sort(key=lambda x:math.inf if x is '_' else x)
        return len(dict.keys())

nums = [0,0,1,1,1,2,2,3,3,4]

print(Solution().removeDuplicates(nums))
print()