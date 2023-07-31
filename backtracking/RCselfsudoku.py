def valid(i, j):
    return (i//9 == j//9) or (i-j) % 9 ==0 or (i//27 == j // 27 and i%9//3 == j%9//3 )
def solve(board):
    ans=[]
    idx = board.index('.') if ('.') in board else -1
    if idx ==-1:
        return [board]
    exclude = {board[i] for i in range(81) if valid(idx, i)}
    for m in set('123456789') - exclude:
        ans += solve(board[:idx]+[m]+board[idx+1:])
    return ans


S= \
["5","3",".",".","7",".",".",".",".",
 "6",".",".","1","9","5",".",".",".",
 ".","9","8",".",".",".",".","6",".",
 "8",".",".",".","6",".",".",".","3",
 "4",".",".","8",".","3",".",".","1",
 "7",".",".",".","2",".",".",".","6",
 ".","6",".",".",".",".","2","8",".",
 ".",".",".","4","1","9",".",".","5",
 ".",".",".",".","8",".",".","7","9"]
 

ans = solve(S)

for i in range(9):
    print(ans[0][i*9:i*9+9])