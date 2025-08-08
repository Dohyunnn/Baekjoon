#부분수열의 합 
#N개의 정수로 이루어진 수열, 부분 수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수 

#풀이
#조합으로 1,2,3,..N개씩 경우의 수를 다 구해서 그 합 체크
from itertools import combinations
N, S = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(1, N+1):
    comb = combinations(arr, i)
    for com in comb:
        if sum(com) == S:
            cnt += 1 
print(cnt)