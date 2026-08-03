class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0
        

        def expand(left, right):
            nonlocal res
            
            if s[left] == s[right]:
                
                res+=1
            
                if left - 1 >= 0 and right + 1 < len(s):
                    expand(left-1, right+1)
        
        for i in range(len(s)):

            expand(i,i)
            if i + 1 < len(s):
                expand(i, i+1)
        
        return res