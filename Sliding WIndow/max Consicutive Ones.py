from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        lo, hi = 0, 0
        zero_cnt = 0
        max_length = 0

        while hi < len(nums):
            if nums[hi] == 0:
                zero_cnt += 1

            while zero_cnt > k:
                if nums[lo] == 0:
                    zero_cnt -= 1
                lo += 1
            
            max_length = max(max_length, hi - lo + 1)
            hi += 1
        return max_length