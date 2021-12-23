# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums: nums.remove(val)
        return len(nums)
        # start = 0
        # end = len(nums) - 1

        # while start <= end:
        #     if nums[start] == val:
        #         nums[start], nums[end], end = nums[end], nums[start], end - 1
        #     else:
        #         start +=1

        # return start

nums = [0,1,2,2,3,0,4,2]

print(Solution().removeElement(nums, 2))

print()