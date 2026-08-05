class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {}
        
        def dp(i):

            if i == len(s):
                memo[i] = True
                return memo[i]
            
            if i in memo:
                return memo[i]
            
            for j in range(i+1, len(s)+1):

                if s[i:j] in wordDict:
                    result = dp(j)
                    if result is True:
                        memo[i] = result
                        return memo[i]
                    
                else:
                    continue
            
            
            memo[i] = False 
            return memo[i]
            
            
                
        
        return dp(0)