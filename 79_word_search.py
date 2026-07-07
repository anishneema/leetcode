class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        def backtrack(i , j, index):

            if index == len(word):
                return True
            
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            
            letter = board[i][j]

            if letter != word[index]:
                return False

            board[i][j] = '#'

            found = (backtrack(i+1, j, index+1) or
            backtrack(i-1, j, index+1) or
            backtrack(i, j+1, index+1) or
            backtrack(i, j-1, index+1))

            board[i][j] = letter 

            return found

        result = False
        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] == word[0]:

                    result = backtrack(i, j, 0)
                    if result:
                        return result
        
        return result