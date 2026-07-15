"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        visited_set = {}

        def dfs(node):

            if node in visited_set:
                return visited_set[node]
            
            node_copy = Node(node.val)

            visited_set[node] = node_copy

            for nodes in node.neighbors:

                node_copy.neighbors.append(dfs(nodes))
            
            return node_copy
        
        if node:
            return dfs(node)

        return node