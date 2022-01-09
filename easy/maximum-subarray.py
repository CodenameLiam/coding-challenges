# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

import math
from typing import List

class Solution:
    def maxSubArray(self, nums):
        cur_max, max_till_now = 0, -math.inf
        for c in nums:
            cur_max = max(c, cur_max + c)
            max_till_now = max(max_till_now, cur_max)
        return max_till_now

nums = [-2]

print(Solution().maxSubArray(nums))