from collections import deque 

N, M = map(int, input().split())
graph = [list(map(int, input()))for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 

def bfs(x,y,cnt):
    q = deque()
    q.append((x,y,cnt))
    visited[x][y] = True 
    
    while q :
        x, y, cnt = q.popleft()
        if x == N-1 and y == M-1:
            return cnt
        
        for i in range(4):
            nx = dx[i] + x 
            ny = dy[i] + y 
        
            if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
                continue 
            if not visited[nx][ny] and graph[nx][ny]:
                q.append((nx,ny, cnt+1))
                visited[nx][ny] = True 
                
            
        
        
if graph[0][0]:
    print(bfs(0,0,1))
    
else:
    print(0)
    