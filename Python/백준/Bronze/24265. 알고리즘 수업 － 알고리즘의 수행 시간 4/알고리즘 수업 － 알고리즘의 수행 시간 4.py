import sys
count = int(sys.stdin.readline())
sum = 0
for i in range(count-1):
    sum += count-(i+1)
print(sum)
print(2)