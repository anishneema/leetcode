class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_occur = {}

        for i in range(len(s)):

            last_occur[s[i]] = i

        
        end = 0
        ans = []
        total = 0
        
        for i in range(len(s)):

            char = s[i]
            end = max(end, last_occur[char])

            if end == i:

                ans.append(i+1 - total)
                total = i+1
        

        return ans