class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        maxlength = 0

        def expand(left, right):

            nonlocal res, maxlength

            if s[left] == s[right]:

                if right - left + 1 > maxlength:
                    maxlength = right - left + 1
                    res = s[left:right+1]
                
                if left - 1 >= 0 and right + 1 < len(s):

                    

                    expand(left-1, right+1)
                    
        



        for i in range(len(s)):


            expand(i,i)

            if i+1 < len(s):
                expand(i,i+1)
        
        return res