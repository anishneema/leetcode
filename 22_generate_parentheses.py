class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(curr, openp, close):

            if openp + close == n*2:
                ans.append("".join(curr[:]))
                return


            if openp < n:
                curr.append('(')
                backtrack(curr, openp + 1, close)
                curr.pop()
            if close < openp:
                curr.append(')')
                backtrack(curr, openp, close + 1)
                curr.pop()
        
        ans = []
        backtrack([], 0 , 0)
        return ans