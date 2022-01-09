# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

from typing import List
from functools import cache

class Solution:

    def canJump(self, nums: List[int]) -> bool:

        # # Recursive (not hashable tho)
        # if len(nums) <= 1:
        #     return True

        # for i in range(nums[0], 0, -1):
        #     if self.canJump(nums[i:]):
        #         return True

        # return False


        # # Dynamic programming
        # n = len(nums)

        # @cache
        # def jump(i: int) -> bool:
        #     # Current index is the last index in the array
        #     if i == n - 1:
        #         return True

        #     # Explore traversial options
        #     for j in range(i+1, min(n-1, i + nums[i]) + 1):
        #         if jump(j):
        #             return True

        #     # No jumps exist where we can reach that last index
        #     return False

        # # Start traversing from the root index
        # return jump(0)


        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i


        return goal == 0






                

# nums = [8, 1, 2]
# nums = [2,3,1,1,4]
# nums = [1,2,3]
# nums = [3,2,1,0,4]
# nums = [3,0,8,2,0,0,1]
# nums = [3,0,0,0,0,0,8,0,0,1]
# nums = [1, 2, 4]
# nums = [0]
# nums = [2, 0, 0]
nums = [5,9,3,2,1,0,2,3,3,1,0,0]

print(Solution().canJump(nums))