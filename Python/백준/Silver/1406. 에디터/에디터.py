import sys
from collections import deque

word = sys.stdin.readline()
stack = []
for i in range(len(word)-1):
    stack.append(word[i])
stack2 = deque()
count = int(sys.stdin.readline())
for i in range(count):
    letter = list(sys.stdin.readline().split())
    if(letter[0] == 'L'):
        if(len(stack)<1):
            continue
        stack2.appendleft(stack.pop())
    elif(letter[0] == 'D'):
        if(len(stack2)<1):
            continue
        stack.append(stack2.popleft())
    elif(letter[0] == 'B'):
        if(len(stack)<1):
            continue
        stack.pop()
    else:
        stack.append(letter[1])
print("".join(stack+list(stack2)))