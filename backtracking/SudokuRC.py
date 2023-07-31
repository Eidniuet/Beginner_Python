def is_valid(i,j)
    return
def same_row(i,j): return (i//9 == j//9)
def same_col(i,j): return (i-j) % 9 == 0
def same_block(i,j): return (i//27 == j//27 and i%9//3 == j%9//3)

def solveSudoku(board):
    ans = []
    idx = board.index('.') if '.' in board else -1
    if idx == -1: #解完了
        return [board]
    exclude = {board[j] for j in range(81) if same_row(idx,j) or same_col(idx,j) or same_block(idx,j)}
    for m in set('123456789')-exclude:
        ans += solveSudoku(board[:idx]+[m]+board[idx+1:])
    return ans

sudoku= \
["5","3",".",".","7",".",".",".",".",
 "6",".",".","1","9","5",".",".",".",
 ".","9","8",".",".",".",".","6",".",
 "8",".",".",".","6",".",".",".","3",
 "4",".",".","8",".","3",".",".","1",
 "7",".",".",".","2",".",".",".","6",
 ".","6",".",".",".",".","2","8",".",
 ".",".",".","4","1","9",".",".","5",
 ".",".",".",".","8",".",".","7","9"]
 
import time
tStart = time.time()#計時開始
print(solveSudoku(sudoku))
tEnd = time.time()#計時結束
print("Total time= %f seconds" % (tEnd - tStart))