import sys

def binarySearch(target):
    start = 0
    end = len(aList)-1
    while start<=end:
        mid = (start+end)//2
        if(target==aList[mid]):
            return 1
        elif(aList[mid]>target):
            end = mid-1
        else:
            start = mid+1
    return 0

firstCount = int(sys.stdin.readline())
aList = list(map(int,sys.stdin.readline().split()))
aList.sort()
secondCount = int(sys.stdin.readline())
mList = list(map(int,sys.stdin.readline().split()))
for i in range(secondCount):
    print(binarySearch(mList[i]))