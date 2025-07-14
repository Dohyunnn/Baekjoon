#유기농 배추 - bfs 
from collections import deque 
T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x,y))
    visited[y][x] = True
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N: 
                if visited[ny][nx]:
                    continue
                if graph[ny][nx]:
                    q.append((nx, ny))
                    visited[ny][nx] = True      

for _ in range(T): 
    M, N, K = map(int, input().split())
    graph = [[False]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    cnt = 0
    for i in range(K):
        x, y = map(int, input().split())
        graph[y][x] = True     

    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue 
            if graph[i][j]:
                bfs(j, i)
                cnt += 1
    print(cnt)

                    
                    










