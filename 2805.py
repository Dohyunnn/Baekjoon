#나무자르기
#파라매트릭 이분탐색 
#자를 수 있는 나무 높이의 최대를 구하는것 (가능한 개수를 최소로)
#가능한 step에서 cur을 계속 늘리면서 해당 높이가 원하는 만큼 자를 수 있으면 계속 True 반환, 아니면 step이 반씩 줄고, step이 0이 될 떄 cur은 자를 수 있는 높이의 최대로 남아있음
def is_possible(h):
    global N, M, trees
    total = 0
    
    for tree in trees:
        if tree > h:
            total += (tree - h)
    return (total >= M )


N, M = map(int, input().split())
trees =list(map(int, input().split()))

cur = -1 
step = int(1e9)+1

while step:
    while (cur+step <= int(1e9)) and is_possible(cur + step):
        cur += step
    step //= 2  
    
print(cur)