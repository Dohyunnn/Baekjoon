from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = True 
    cnt = 0  
                     
    while q:
        cur = q.popleft() 
        cnt += 1   
        for y in graph[cur]:
            if visited[y]:
                continue
            q.append(y)
            visited[y] = True
    
    return cnt 
print(bfs(1) -1)    
