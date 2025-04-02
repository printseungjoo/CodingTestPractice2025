import sys

n,p = map(int, sys.stdin.readline().split())
pList = [[] for i in range(6)]
answer = 0
count= 0
for i in range(n):
    n1,p1 = map(int,sys.stdin.readline().split())
    same = False
    count2 = 0
    if (len(pList[n1-1]) == 0):
        pList[n1-1].append(p1)
        answer+=1
    else:
        while pList[n1-1] and pList[n1-1][-1]>p1:
            pList[n1-1].pop()
            answer+=1
        if not pList[n1-1] or pList[n1-1][-1]!=p1:
            pList[n1-1].append(p1)
            answer+=1
            
print(answer)