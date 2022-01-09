# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0
        for i in range(1, len(height) - 1):
            currentHeight = height[i]
            leftWall = max(height[:i])
            rightWall = max(height[i+1:])

            if leftWall > currentHeight and rightWall > currentHeight:
                trapped += (min(leftWall, rightWall) - currentHeight)
           
        return trapped  


# height = [2,1,0,1,3]
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]

print(Solution().trap(height))