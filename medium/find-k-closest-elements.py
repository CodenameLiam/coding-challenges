from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        
        while l < r:
            m = (l + r) // 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else: 
                r = m
        return arr[l:l+k]

# Example 1
arr = [1,2,3,4,5]
k = 2
x = 3

# # Example 2
# arr = [1,2,3,4,5]
# k = 4
# x = -1

# Example 3
arr = [1,1,2,2,2,2,2,3,3]
k = 3
x = 3
        

print(Solution().findClosestElements(arr, k, x))