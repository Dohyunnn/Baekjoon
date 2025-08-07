import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = list(map(int, input().split()))

right = -1 
cur_sum = 0
answer = 0
for left in range(N):
    while (right+1 < N) and cur_sum + arr[right+1] <= M:   #애초에 다음 right이 들어갈 수 있어야 탐색
        right += 1                                         #right 확장하면서 계속 반복
        cur_sum += arr[right]
        
    if cur_sum == M:                                    #그러다 다음 right이 못들어가면 현재 값 체크
        answer += 1 
    
    cur_sum -= arr[left]     #while이 끝나면 다음 left 탐색 들어가야하니 , 현재 left를 합에서 빼줌
    
    
print(answer)