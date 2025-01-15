class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(speed):
            total_time = 0
            for num in piles:
                total_time += (num + speed - 1) // speed  
            return total_time <= h
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if can_finish(mid):
                hi = mid  
            else:
                lo = mid + 1  
        return lo