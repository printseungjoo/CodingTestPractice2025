import sys
count = int(sys.stdin.readline())
for i in range(count):
    classList = list(map(int,sys.stdin.readline().split()))
    numClass = classList[0]
    sortedList = sorted(classList[1:])
    sum = sortedList[1]-sortedList[0]
    for j in range(1,numClass-1):
        if(sum<sortedList[j+1]-sortedList[j]):
            sum = sortedList[j+1]-sortedList[j]
    print("Class "+str(i+1))
    print("Max "+str(sortedList[-1])+", Min "+str(sortedList[0])+", Largest gap "+str(sum))