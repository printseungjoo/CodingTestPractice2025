import sys

count = 0
secondAnswer = 0

def dfs(i,j):
    stack = [(i,j)]
    count2 = 0
    while stack:
        i,j = stack.pop()
        if 0<=i<m and 0<=j<n and pList[j][i]==1:
            pList[j][i]=0
            count2+=1
            stack.append((i+1,j))
            stack.append((i-1,j))
            stack.append((i,j+1))
            stack.append((i,j-1))
    return count2

n,m = map(int, sys.stdin.readline().split(' '))
pList = []
for i in range(n):
    pList.append(list(map(int,sys.stdin.readline().split(' '))))
for j in range(n):
    for i in range(m):
        if pList[j][i]==1:
            secondAnswer = max(dfs(i,j),secondAnswer)
            count+=1
print(count)
print(secondAnswer)