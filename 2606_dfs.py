# 바이러스 
# dfs ver 
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
from collections import deque 

N = int(input())
M = int(input())
graph = [[False] * N for _ in range(N)]
visited = [False] * N 


for i in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = True
    graph[b-1][a-1] = True 

cnt = 0
def dfs(x):
    global cnt
    visited[x] = True 

    for i in range(N):
        if visited[i]:
            continue
        if graph[x][i]: 
            cnt += 1
            dfs(i)

dfs(0)
print(cnt)


