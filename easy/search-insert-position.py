# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
import math
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # # Sequential (Shit)
        # i = 0
        # if target > nums[-1]:
        #     return len(nums)
        # while target > nums[i]:
        #     if nums[i] == target:
        #         return i
        #     i += 1
        # return i

        # Binary (Gucci)
        low = 0
        high = len(nums)

        while low < high:
            mid = low + math.floor((high - low)/2)
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        return low

nums = [1,3,5,6]
target = 7

print(Solution().searchInsert(nums, target))