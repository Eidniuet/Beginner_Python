def frogmove(frog, move=()):
    if frog==[-1,-1,-1,0,1,1,1]:
        return[move]
    ans = []
    length = len(frog)
    for i in range(length):
        if i < length - 2 and frog[i] == 1 and frog[i+1] ==-1 and frog [i+2] ==0:
            new_frog = frog[:]
            new_frog[i], new_frog[i+2] = new_frog[i+2], new_frog[i]
            ans += frogmove(new_frog, move+(i+1, "Jump Right"))

        if i > 1 and frog[i] == -1 and frog[i-1] ==1 and frog [i-2] ==0:
            new_frog = frog[:]
            new_frog[i], new_frog[i-2] = new_frog[i-2], new_frog[i]
            ans += frogmove(new_frog, move+(i+1, "Jump Left"))

        if i < length -1 and frog[i] == 1 and frog[i+1] ==0:
            new_frog = frog[:]
            new_frog[i], new_frog[i+1] = new_frog[i+1], new_frog[i]
            ans += frogmove(new_frog, move+(i+1, "Move Right"))

        if i > 0 and frog[i] == -1 and frog[i-1] ==0:
            new_frog = frog[:]
            new_frog[i], new_frog[i-1] = new_frog[i-1], new_frog[i]
            ans += frogmove(new_frog, move+(i+1, "Move Left"))
    return ans

frog = [1,1,1,0,-1,-1,-1]
print(frogmove(frog))
            