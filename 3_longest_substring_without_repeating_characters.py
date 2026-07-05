class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hashmap = {}
        longest = 0
        l = 0

        for r in range (len(s)):

            if (s[r] in hashmap):

                l = max(l, hashmap[s[r]] + 1)
             
            
            longest = max(longest, r-l + 1)
            hashmap[s[r]] = r
        
        return longest