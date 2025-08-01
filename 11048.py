import sys
sys.setrecursionlimit(1000000)   #입력이 1000까지라 재귀 깊이 늘려주기, 파이썬의 재귀함수 최대 깊이는 1000

N,M = map(int, input().split())

dp = [[0] + list(map(int, input().split())) for _ in range(N)] 
dp = [[0] * (M+1)] + dp  #맨 위에 0으로 채우기 


for i in range(1,N+1):
    for j in range(1, M+1):
        dp[i][j] += max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
print(dp[N][M])