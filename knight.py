class KnightMove:
    def __init__ (self, r ,c):
        self.r = r
        self.c = c
        self.board = [[0 for x in range(r)] for x in range(c)]
        self.dirs = [(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2)]
        self.find = False
    
    def isValid(self,pos):
        return (0<=pos[0]<=7  and 0<=pos[1]<=7 and self.board[pos[0]][pos[1]]==0)
        
    def value(self, pos):
        return min(pos[0],self.r-pos[0]-1)+min(pos[1],self.c-pos[1]-1)

    def Move(self,pos, curstep=1):
        self.board[pos[0]][pos[1]]=curstep
        
        if curstep ==64:
            for i in range (8):
                print(' '.join([f"{self.board[i][j]:2d}" for j in range(8)]))
            
            self.find = True
        else:
            nextpos = [[pos[0]+d[0], pos[1]+d[1]] for d in self.dirs]
            nextpos = sorted(filter(lambda x:self.isValid(x), nextpos), key =lambda x : self.value(x))
            for d in nextpos:
                if not self.find:
                    self.Move(d, curstep+1)
        self.board[pos[0]][pos[1]] = 0

startPos = (0,7)
solver = KnightMove(8,8)
solver.Move(startPos)