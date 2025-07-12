#유기농 배추 - dfs
import sys
sys.setrecursionlimit(10**6)
T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):
    visited[y][x] = True 
    #print(f'new dfs x:{x},y:{y}')
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if visited[ny][nx]:
                continue
            if graph[ny][nx]:
                dfs(nx, ny)


for _ in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    graph = [[False]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    
    for _ in range(K):  
        x, y = map(int, input().split())
        graph[y][x] = True

    for y in range(N):
        for x in range(M):
            if not visited[y][x] and graph[y][x]: 
                dfs(x,y)
                cnt += 1 
    

    print(cnt)