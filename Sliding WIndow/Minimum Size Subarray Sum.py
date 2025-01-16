from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        curr_sum = 0
        ans = float('inf')
        
        for end in range(len(nums)):
            curr_sum += nums[end]

            while curr_sum >= target:
                ans = min(ans, end - start + 1)
                curr_sum -= nums[start]
                start += 1

        if ans == float('inf'):
            return 0
        else:
            return ans
