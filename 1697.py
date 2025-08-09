from collections import deque
N , K = map(int, input().split())

max = int(1e5)
visited = [False] * (max+1)

def bfs(N, cnt):
    q = deque()
    q.append((N, cnt))
    visited[N] = True
    
    while q :
        cur, cnt = q.popleft()
        next = [cur+1, cur-1, cur*2]
        
        if cur == K:
            return cnt
        
        for n in next:
            if 0 <= n <= max and not visited[n]:
                q.append((n, cnt +1))
                visited[n] = True 

result = bfs(N, 0) 
print (result)
