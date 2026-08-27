class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            column = []
            empty_fields = board[i].count('.')
            if empty_fields==0:
                empty_fields=1
            if len(set(board[i]))+empty_fields-1 != 9:
                return False
            for j in range(9):
                column.append(board[j][i])
            empty_fields = column.count('.')
            if empty_fields==0:
                empty_fields=1
            if len(set(column))+empty_fields-1 != 9:
                return False
        for i in range(1,9,3):
            for j in range(1,9,3):
                field = [
                    board[i-1][j-1],
                    board[i-1][j],
                    board[i-1][j+1],
                    board[i][j-1],
                    board[i][j],
                    board[i][j+1],
                    board[i+1][j-1],
                    board[i+1][j],
                    board[i+1][j+1]
                ]
                empty_fields = field.count('.')
                if empty_fields==0:
                    empty_fields=1
                if len(set(field))+empty_fields-1 != 9:
                    return False
        return True
