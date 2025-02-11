import sys
count = int(input())
numList = list(map(int,sys.stdin.readline().split()))
answer = [-1]*count
stack = list()
stack.append(0)
for i in range(1,count):
    while stack and numList[stack[-1]]<numList[i]:
        answer[stack.pop()] = numList[i]
    stack.append(i)
print(*answer)