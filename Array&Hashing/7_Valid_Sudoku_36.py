class Solution:
    # Validate a single 3x3 square
    def verifySquare(self, board:list[list[str]], row: int, col: int) -> bool:
        test = set()
        for i in range(3):
            for j in range(3):
                if board[row + i][col + j] == ".":
                    continue
                if board[row + i][col + j] in test:
                    return False
                else:
                    test.add(board[row + i][col + j])
        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Validate a row
        for row in board:
            test = set()
            for i in row:
                if i == ".":
                    continue
                if i in test:
                    return False
                else:
                    test.add(i)
        
        # Validate a column
        for colind in range(9):
            test = set()
            for colrow in range(9):
                if board[colrow][colind] == ".":
                    continue
                if board[colrow][colind] in test:
                    return False
                else:
                    test.add(board[colrow][colind])
        
        # Validate the squares using a support function
        for x in range(3):
            for y in range(3):
                if not Solution.verifySquare(self, board, 3*x, 3*y):
                    return False

        return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(Solution.isValidSudoku(Solution,board))

s="CIAO"
