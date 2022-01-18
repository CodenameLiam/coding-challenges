from collections import deque
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = deque()

        leftPointer = 0
        rightPointer = len(nums) - 1

        while leftPointer <= rightPointer:
            leftSquared = pow(nums[leftPointer], 2)
            rightSquared = pow(nums[rightPointer], 2)

            if leftSquared > rightSquared:
                res.appendleft(leftSquared)
                leftPointer += 1
            else:
                res.appendleft(rightSquared)
                rightPointer -= 1

        return list(res)


nums = [-7,-3,2,3,11]
print (Solution().sortedSquares(nums))