import sys
sys.setrecursionlimit(10000)

def dfs(i,j):
    if i<0 or j<0 or i>=n or j>=m:
        return False
    if(bList[i][j]==1):
        bList[i][j]=0
        dfs(i-1,j)
        dfs(i,j-1)
        dfs(i+1,j)
        dfs(i,j+1)
        return True
    return False

loop = int(sys.stdin.readline())
for k in range(loop):
    m,n,kNum = map(int,sys.stdin.readline().split())
    bList = [[0]*(m) for _ in range(n)]
    answer = 0
    for i in range(kNum):
        m1,n1 = map(int,sys.stdin.readline().split())
        bList[n1][m1] = 1
    for i in range(n):
        for j in range(m):
            count = 0
            if dfs(i,j):
                answer+=1
    print(answer)