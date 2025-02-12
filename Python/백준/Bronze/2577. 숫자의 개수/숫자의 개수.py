import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
abc = list(map(int,str(a*b*c)))
l = [0]*10
for i in range(len(abc)):
    l[abc[i]]+=1
for i in range(10):
    print(l[i])