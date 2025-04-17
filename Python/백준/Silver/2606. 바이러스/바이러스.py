import sys

computerNum = int(sys.stdin.readline())
forNum = int(sys.stdin.readline())
graph = {}
answer = 0

def dfs(graph, start_node):
    global answer
    visited = set()
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            answer+=1
            if node in graph:
                stack.extend(reversed(graph[node]))
    return list(visited)

for _ in range(forNum):
    u,v = map(int,sys.stdin.readline().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

dfs(graph, 1)
print(answer-1)