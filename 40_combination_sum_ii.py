class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtracking(curr, i, total):


            if total == target:
                ans.append(curr[:])
                return
            
            for j in range(i, len(candidates)):

                if j > i and candidates[j] == candidates[j-1]:
                    continue

                if total + candidates[j] > target:
                    return
                
                curr.append(candidates[j])
                backtracking(curr, j+1, total + candidates[j])
                curr.pop()
            
        candidates.sort()
        ans = []
        backtracking([], 0, 0)
        return ans