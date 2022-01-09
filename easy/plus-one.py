# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return  [int(i) for i in str(int(''.join([str(elem) for elem in digits])) + 1)]
    
digits = [1,9,9]
print(Solution().plusOne(digits))