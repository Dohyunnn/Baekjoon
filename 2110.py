# 공유기 설치 - 파라메트릭 서치
import sys
input = lambda: sys.stdin.readline().rstrip()  

N, C = map(int, input().split())
houses = sorted([int(input()) for _ in range(N)])

def is_possible(d):
    before = 0      #이 문제는 첫번째 집은 무조건 설치한다고 봐도 문제 없고, 유리함  
    cnt = 1 
    
    for current in range(1, N):  
        if houses[current] - houses[before] >= d:    # 찾는 거리의 이상이면 상관 없음 
            before = current
            cnt += 1 
        
    return (cnt >= C)   #원하는 공유기 수 이상으로 설치 가능하면 True  

cur = -1 
step = int(1e9) + 1

while step:
    while (cur + step) <= int(1e9) and is_possible(cur + step):
        cur += step 
    step //= 2 
    
print(cur)
