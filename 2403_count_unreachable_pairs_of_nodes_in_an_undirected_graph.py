class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        visited = set()
        count = []
        size = 0

        adj = {i:[] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):

            nonlocal size

            visited.add(node)
            size+=1
            
            for nodes in adj[node]:

                if nodes not in visited:
                    dfs(nodes)
                    
            
            
            
        

        for i in range(n):

            if i not in visited:
                size = 0
                dfs(i)
                count.append(size)
        
        res = 0
        total = 0

        for c in count:
            res += c * total
            total += c
        
        return res