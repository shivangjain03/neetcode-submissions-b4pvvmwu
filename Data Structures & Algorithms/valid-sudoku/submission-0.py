class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row check
        for i in board:
            seen = {}
            for j in i:
                if j.isnumeric():
                    if j in seen:
                        return False
                    else:
                        seen[j] = 1
        
        # Col check
        for i in range(0,9):
            seen = {}
            for j in board:
                if j[i].isnumeric():
                    if j[i] in seen:
                        return False
                    else:
                        seen[j[i]] = 1
        

        # Box check 
        for z in range(9):
            seen = {}
            for i in range(3):
                for j in range(3):
                    row = (z//3) * 3 + i
                    col = (z % 3) * 3 + j

                    if board[row][col].isnumeric():
                        if board[row][col] in seen:
                            return False
                        else:
                            seen[board[row][col]] = 1

        return True
                            
        

        