import sys
sys.setrecursionlimit(100000)

def dfs(graph,start,visited):
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(graph,node,visited)

count = 0
n,m = map(int,sys.stdin.readline().split())
l = [[] for i in range(n+1)]
for i in range(m):
    l1,l2 = map(int,sys.stdin.readline().split())
    l[l1].append(l2)
    l[l2].append(l1)
visited = [False]*(n+1)
for i in range(1,n+1):
    if not visited[i]:
        dfs(l,i,visited)
        count+=1
print(count)