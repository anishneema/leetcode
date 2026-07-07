class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        
        def backtracking(curr, start):

            if start == len(s):
                ans.append(curr[:])
                return
        
            #try every substring in the current string
            for end in range(start, len(s)):
                
                #is this substring a palindrome
                if palindrome(s[start:end+1]):

                    #append the substring
                    curr.append(s[start:end+1])

                    #try to find more palindromes in the smaller strings
                    backtracking(curr, end+1)
                    curr.pop()

                    

                

        def palindrome(s):

            l = 0
            r = len(s)-1

            while l <= r:

                if s[r] != s[l]:
                    return False
                l+=1
                r-=1
            
            return True

        ans = []
        backtracking([], 0)
        return ans