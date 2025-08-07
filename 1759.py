from itertools import combinations

vows = ['a', 'e', 'i', 'o', 'u']   #모음

def is_possible(word):
    global L, C, arr

    vow = 0
    for w in word:       #조합된 word에  
        if w in vows:    #모음이 있으면
            vow += 1     #개수 체크 
    con = L - vow  #모음은 조합된 word에서 모음 뺸 길이
    
    return (vow >= 1 and con >=2 ) #True or False    
    
L, C = map(int, input().split())
arr = input().split()

arr.sort()  #사전순으로 필요, 미리 정렬해놓고 combinations하기 
password = combinations(arr,L)
#조합 모든 경우
for word in password:          #하나씩 확인해보기
    if is_possible(word):      #True면
        print(''.join(word))