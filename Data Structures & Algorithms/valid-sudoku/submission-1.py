class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            empty_fields = row.count('.')
            if empty_fields==0:
                empty_fields=1
            if len(set(row))+empty_fields-1 != 9:
                return False
        for i in range(9):
            column = []
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
