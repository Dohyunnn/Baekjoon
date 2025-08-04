#LIS 가장 긴 증가하는 부분 수열

N = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0] * (N+1)
dp[1] = 1

for last in range(2, N+1):
    path = 0
    for front in range(1, last):
        if arr[last] > arr[front]:
            path = max(path, dp[front])
    dp[last] = path + 1
    
print(max(dp))
    