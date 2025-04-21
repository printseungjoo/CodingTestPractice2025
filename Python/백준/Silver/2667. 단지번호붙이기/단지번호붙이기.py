import sys

n = int(sys.stdin.readline())
square = []
for i in range(n):
    square.append(list(map(int,sys.stdin.readline().strip())))
answer = 0
answerList = []

def dfs(i,j):
    global answer
    global answerList
    if i<0 or j<0 or i>=n or j>=n:
        return False
    if square[i][j]==1:
        answer+=1
        square[i][j]=0
        dfs(i+1,j)
        dfs(i,j+1)
        dfs(i-1,j)
        dfs(i,j-1)
    return True

for i in range(n):
    for j in range(n):
        answer = 0
        dfs(i,j)
        if(answer!=0):
            answerList.append(answer)

print(len(answerList))
answerList.sort()
for i in range(len(answerList)):
    print(answerList[i])