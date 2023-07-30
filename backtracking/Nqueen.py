def check (state, nextrow):
    nextcol = len(state)
    return any(abs(state[i]-nextrow) in (0, nextcol-i) for i in range(nextcol)) # check row and 

def queen(n, state):
    if len(state) == n:
        return [()]
    ans=[]
    for pos in range(n):
        if not check(state, pos):
            ans += [(pos,) + result for result in queen(n, state +(pos,))]
    return ans