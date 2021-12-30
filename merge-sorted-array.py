from typing import List


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

nums1 = [0]
m = 0
nums2 = [1]
n = 1

nums1 = [0, 0]
m = 0
nums2 = [1, 5]
n = 2

# nums1 = [0,0,0,0,0]
# m = 0
# nums2 = [1,2,3,4,5]
# n = 5

# nums1 = [-1,0,0,3,3,3,0,0,0]
# m = 6
# nums2 = [1,2,2]
# n = 3




class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        



Solution().merge(nums1, m, nums2, n)

print(nums1)