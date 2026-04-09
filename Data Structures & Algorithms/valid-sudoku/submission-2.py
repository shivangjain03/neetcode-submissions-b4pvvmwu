class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row check: O(n^2)
        for i in board:
            dict1 = {}
            for j in i:
                if j.isalnum():
                    if j in dict1:
                        return False
                    else:
                        dict1[j] = 1
        
        #Col check O(n^2)
        for i in range(9):
            dict1 = {}
            for j in range(9):
                if board[j][i].isalnum():
                    if board[j][i] in dict1:
                        return False
                    else:
                        dict1[board[j][i]] = 1
        
        #Box check
        dict1 = {}
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val.isalnum():
                    box_id = (i//3, j//3)
                    if box_id not in dict1:
                        dict1[box_id] = []
                    if val in dict1[box_id]:
                        return False 
                    else:
                        dict1[box_id].append(val)
        
        return True

        