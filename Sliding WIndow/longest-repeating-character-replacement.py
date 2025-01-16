class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dictionary = {}
        start = 0
        max_count = 0  
        ans = 0

        for end in range(len(s)):
            dictionary[s[end]] = dictionary.get(s[end], 0) + 1
            max_count = max(max_count, dictionary[s[end]])
            
            while (end - start + 1) - max_count > k:
                dictionary[s[start]] -= 1
                if dictionary[s[start]] == 0:
                    del dictionary[s[start]]
                start += 1
            
            ans = max(ans, end - start + 1)

        return ans