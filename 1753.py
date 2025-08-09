from queue import PriorityQueue
import sys
input = lambda: sys.stdin.readline().rtrip()
#input
INF = int(1e12)

V,E = map(int, input().split())
K = int(input())

lst = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    lst[u].append([v,w])
    
# solve
dist = [INF] * (V+1)
pq = PriorityQueue()
pq.put([0, K])
dist[K] = 0 

while not pq.empty():
    cur_dist, cur_node = pq.get() 
    for adj_node, adj_dist in lst[cur_node]:
        temp = cur_dist + adj_dist 
        if temp < dist[adj_node]:
            pq.put([temp, adj_node])
            dist[adj_node] = temp
            
for d in dist[1:]:
    if d != INF:
        print(d)
    else:
        print('INF')