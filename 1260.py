#bfs dfs 
from collections import deque

N, M, V = map(int, input().split())
graph = [[False]*(N) for _ in range(N)]
visited = [False]*N

for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = True
    graph[b-1][a-1] = True


def dfs(x):
    visited[x] = True
    print(x+1, end=" ")

    for i in range(N):
        if visited[i]:
            continue
        if graph[x][i]:
            dfs(i)

def bfs(x):
    q = deque([x])
    visited2 = [False]*N

    while q:
        x = q.popleft()
        visited2[x] = True
        print(x+1, end=" ")
        #print(f'x:{x}, visited:{visited2}')

        for i in range(N):
            if visited2[i]:
                continue
            if graph[x][i]:
                q.append(i)
                visited2[i] = True
             
dfs(V-1)
print()
bfs(V-1)
