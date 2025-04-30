import sys

firstCount = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
secondCount = int(sys.stdin.readline())
nums2 = list(map(int,sys.stdin.readline().split()))

dict = {}
for i in range(firstCount):
    dict[nums[i]] = 1
for i in range(secondCount-1):
    if dict.get(nums2[i],0)==1:
        print(1, end=' ')
    else:
        print(0, end=' ')
if dict.get(nums2[-1],0)==1:
    print(1)
else:
    print(0)