#유기농 배추 - bfs 
from collections import deque 
T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#def bfs(x, y):
    
    #while q:
    #    x, y = q.popleft()
        
    #    for i in range4:
    



for _ in range(T): 
    M, N, K = map(int, input().split())
    graph = [[False]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    q = deque([])
    
    for i in range(K):
        x, y = map(int, input().split())
        graph[y][x] = True     

        for i in range(N):
            for j in range(M):
                if visited[i][j]:
                    continue 
                if graph[i][j]:
                    q.append((j,i))
                    visited[i][i] = True
                   # bfs(j, i)

                    
                    










