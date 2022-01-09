from typing import List, Set

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        for val in numSet:
            # if val is start of sequence
            if val - 1 not in numSet:
                length = 0
                # iterate through sequence
                while val + length in numSet:
                    length += 1

                # update longest sequence
                longest = max(length, longest)
                


        return longest


# nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]

print(Solution().longestConsecutive(nums))