import sys
from bisect import bisect_left, bisect_right

firstCount = int(sys.stdin.readline())
firstList = list(map(int,sys.stdin.readline().split()))
secondCount = int(sys.stdin.readline())
secondList = list(map(int,sys.stdin.readline().split()))
answer = []
firstList.sort()
for i in range(secondCount):
    answer.append((bisect_right(firstList,secondList[i])-bisect_left(firstList,secondList[i])))
for i in range(len(answer)-1):
    print(answer[i],end=" ")
print(answer[-1])