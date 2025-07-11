# 바이러스
# bfs
'''
  0 1 2 3 4 5 6
0 0 1 0 0 1 0 0  
1 0 0 1 0 1 0 0 
2 0 1 0 0 0 0 0 
3 0 0 0 0 0 0 1
4 1 1 0 0 0 1 0
5 0 0 0 0 1 0 0
6 0 0 0 1 0 0 0
'''
'''
x+1   q 
1 > 2, 5 
2 > 3 5-fail
5 > 1-fail, 2-fail, 6 
3 > 2-fail 
6 > 4-fail 
2, 5, 3, 6이 for문에서 append될 때 cnt+1 
'''

from collections import deque

N = int(input())
M = int(input())
graph = [[False]*N for _ in range(N)]
visited = [False] * N 
cnt = 0

for i in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = True
    graph[b-1][a-1] = True

def bfs(x):
    q = deque([x])
    visited[x] = True
    global cnt
    while q: 
        x = q.popleft()

        for i in range(N):
            if visited[i]:
                continue    
            if graph[x][i]:
                q.append(i)
                cnt +=1 
                visited[i] = True

bfs(0)
print(cnt)
    



