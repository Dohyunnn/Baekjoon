
'''
# 트리 모양
    1               
 4     6                
2 7     3         
         5        
# graph[a][b] 이차원 배열식은 노드 수 최대 10만, 10만*10만 = 100억 칸 생성으로 메모리 초과 
# graph[] 인덱스를 활용해서 graph[a].append(b), graph[b].append(a)로 연결 체크
# 인덱스 순서대로 돌면서 해당 노드 번호를 인덱스로 가지는 visited에 현재 인덱스를 부모 노드로 저장 
# visited가 0인지 체크하는식으로 각 번호에 부모 노드가 다 채워지면 visited 2부터 부모 값 출력

graph = [[] for _ in range(N+1)]
[]
[6, 4]
[4]
[6, 5]
[1, 2, 7]
[3, ]
[1, 3, ]
[4]


# bfs 
1 > 6 4       visited 6 = 1, visited4 = 1
6 > 1 3       visited1 = 6,  visited 3 = 6 
4 > v 2 7      visited2 = 4, visited7 = 4   
1 > v v
3 > v 5        visited5 = 3
2 > v 
7 > v
5 > v     

'''
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
parent = [False] * (N+1)

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(x):
    q = deque()
    q.append(x)
    
    while q:
        x = q.popleft()
        
        for i in graph[x]:
            if not parent[i]:
                parent[i] = x 
                q.append(i)
    
bfs(1)
for i in range(2,N+1):
        print(parent[i])