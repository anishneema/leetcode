class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        m = len(board[0])
        n = len(board)

        tree = PrefixTree()

        for word in words:
            tree.insert(word)


        def backtrack(curr, x, y, node):

            ch = board[x][y]
            curr.append(ch)
            board[x][y] = '#'

            if node.isEnd:
                ans.add("".join(curr[:]))
           
            
            directions = [(-1,0), (1,0), (0,-1), (0,1)]

            for dx, dy in directions:

                nx = x + dx
                ny = y + dy

                if 0<=nx<n and 0<=ny<m and board[nx][ny] in node.children:

                    backtrack(curr, nx, ny, node.children[board[nx][ny]])
            
            curr.pop()
            board[x][y] = ch
        
        ans = set()

        node = tree.root

        for i in range(n):

            for j in range(m):

                if board[i][j] in node.children:

                    backtrack([], i , j, node.children[board[i][j]])
        

        return list(ans)
                



class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):

        node = self.root

        for ch in word:

            if ch not in node.children:
                node.children[ch] = TrieNode()
            
            node = node.children[ch]

        node.isEnd = True