class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        ans = 0
        sett = set()

        for i in range(len(s)):
            while s[i] in sett:
                sett.remove(s[l])
                l += 1
            sett.add(s[i])
            ans = max(ans, i - l + 1)
    
        return ans