#개똥벌레   #이분탐색 
#석순과 종유석을 나누어서 저장하고,
#정렬을 한다 >> 이분탐색 필수 
# for i in range(1부터 H까지) 걸리는 칸 탐색
#bottom은 i이상의 값 첫번째 인덱스를 총 개수에서 빼주면 i 이상 수들로 장애물 걸리는 갯수 나오고
#top은 H - i + 1 바꿔서 찾아주면 똑같이 그 이상의 수들을 찾는다 
#구한 수를 계속해서 최소값을 갱신하고 , 값이 같으면 횟수를 증가 시킨다, 갱신할 땐 횟수를 1로 다시 바꾸기
import sys
from bisect import bisect_left
input = sys.stdin.readline
N, H = map(int, input().split())

bottom = []
top = []

for i in range(N):
    l = int(input())
    if i % 2 == 0 :
        bottom.append(l)
    else:
        top.append(l)
        
top.sort()
bottom.sort()

min_value = N 
min_cnt = 0 

for i in range(1,H+1):
    bottom_min = len(bottom) - bisect_left(bottom, i)
    top_min = len(top) - bisect_left(top, H - i + 1)
    total = bottom_min + top_min 
    
    if total < min_value:
        min_value = total
        min_cnt = 1 
    elif total == min_value:
        min_cnt += 1 
        
print(min_value, min_cnt)