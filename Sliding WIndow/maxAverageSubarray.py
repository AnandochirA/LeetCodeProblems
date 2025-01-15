from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0

        for i in range (0, k):
            sum += nums[i]
        ans = sum / k

        for i in range (k, len(nums)):
            sum += nums[i]
            sum -= nums[i - k]
            ans = max(ans, sum / k)
            
        return ans
