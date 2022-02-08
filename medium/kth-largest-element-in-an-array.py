from heapq import heapify, heappop
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

    

        return heapq.nlargest(k, nums)[-1]

        # heapify(nums)
        # for _ in range(len(nums) - k):
        #     heappop(nums)
        # return nums[0]

# Example 1
nums = [3,2,1,5,6,4]
k = 2

# Example 2
nums = [3,2,3,1,2,4,5,5,6]
k = 4


print(Solution().findKthLargest(nums, k))