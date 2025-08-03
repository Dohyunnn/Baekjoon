# N과M (1), 백트래킹 + DFS 
N,M = map(int, input().split())
visited = [False] * (N+1)
path = []

def backtrack(path, visited):
    if len(path) == M:
        print(' '.join(map(str, path)))
        return 
    
    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = True
            backtrack(path + [i], visited)
            visited[i] = False




backtrack(path, visited)         
