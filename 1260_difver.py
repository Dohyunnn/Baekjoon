# dfs와 bfs diffrent version 
from collections import deque

N, M, V = map(int, input().split())
graph = [[False] *(N+1) for _ in range(N+1)]
visited = [False]* (N+1)
visited2 =  [False]* (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

def dfs(x):
    visited[x] = True 
    print(x, end=' ')
    for y in range(1, N+1):
        if visited[y]:
            continue
        if graph[x][y]:
            dfs(y)

def bfs(V):
    q =deque([V])
    visited2[V] = True

    while q:
        V = q.pop(0)
        print(V, end = ' ')
        
        for i in range(1, N+1):    
            if visited2[i] == True:
                continue
            if graph[V][i] == True:
                q.append(i) 
                visited2[i] = True

dfs(V)
print()
bfs(V)