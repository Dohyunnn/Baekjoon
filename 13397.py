import sys 
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = list(map(int, input().split()))

def can_divide(K):
    group_min = arr[0]
    group_max = arr[0]
    group_cnt = 1
    
    for i in range(1, N):
        group_min = min(group_min, arr[i])
        group_max = max(group_max, arr[i])
        
        if group_max - group_min > K:
            group_cnt += 1 
            group_min = arr[i]
            group_max = arr[i]
            
    return group_cnt <= M      
    
min_k  = 0
max_k = max(arr) - min(arr)
answer = max_k 

while min_k <= max_k:
    mid = (min_k + max_k) // 2 
    
    if can_divide(mid):
        answer = mid 
        max_k = mid - 1
    else:
        min_k = mid + 1 
print(answer)
        