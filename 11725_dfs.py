'''
graph = [[] for _ in range(N+1)]
[]
[6, 4]
[4]
[6, 5]
[1, 2, 7]
[3, ]
[1, 3, ]
[4]

# dfs 
1 > 6 visited 6=1 
6 > 3 visited 3 = 6 
3 > 5 visited 5 = 3 
5
3
6
1 > 4 visited 4 = 1
4 > 2 visited 2 = 4 
2 
4 > 7 visited 7 = 4
7
4
3
4
1
끝 
'''
import sys
sys.setrecursionlimit(10**6) # 재귀 제한 풀기 

N = int(input())
graph = [[] for _ in range(N+1)]
parent = [False] * (N+1)

for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())    #입력 10만 이상일 때 input()대신 
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(x):

    for i in graph[x]:
        if not parent[i]:
            parent[i] = x
            dfs(i)

dfs(1)
for i in range(2,N+1):
    print(parent[i])