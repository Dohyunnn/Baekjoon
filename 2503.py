from itertools import permutations
N = int(input())
arr =[input().split()for _ in range(N)]

permu = permutations(range(1,10), 3)
total = 0
for per in permu:
    valid = True   #하나의 per 검색 시작, True
    for num, st, b in arr:
        st_cnt = 0
        b_cnt = 0
        
        for i in range(3):
            if str(per[i]) == num[i]:
                st_cnt += 1
            elif str(per[i]) in num:
                b_cnt += 1
        if st_cnt != int(st) or b_cnt != int(b):    #물어본 질문중에 하나라도 틀리면 답이 아닌것
            valid = False                           #현재 탐색중인 per은 탈락
            break                                    #질문리스트 더 볼 필요가 없어짐
    if valid:
        total += 1
print(total)