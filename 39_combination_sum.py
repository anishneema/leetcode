class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtracking(curr, i, total):

            candidates.sort()

            if total == target:
                ans.append(curr[:])
                return
            

            for i in range(i, len(candidates)):

                if total + candidates[i] > target:
                    return
                
                curr.append(candidates[i])
                backtracking(curr, i, total + candidates[i])
                curr.pop()
            
        
        ans = []
        backtracking([], 0, 0)
        return ans