import sys

class Solution:
    def mySqrt(self, x: int) -> int:

        # r = x
        # while r*r > x:
        #     r = (r + x/r) / 2
        # return r

        # base case
        if x == 0:
            return x

        left = 1
        right = sys.maxsize

        while True:
            mid = left + (right - left) / 2
            if mid > x / mid:
                right = mid - 1
            else:
                if (mid + 1) > x / (mid + 1):
                    return mid
                else:
                    left = mid + 1


print(Solution().mySqrt(9))