#행운의 문자열
#인접해 있는 모든 문자가 같지 않은 문자열 = 행운 문자열
#입력 받은 문자열을 재배치 했을 때 행운 문자열이 몇개 나오는지, 현재 행운이면 이것도 개수에 포함

import sys  
input = sys.stdin.readline  

def dfs(pre_word, length):  
    global counter, result, S 
    
    if length == len(S):  
        result += 1 
        return 
     
    for key in counter.keys():  
        if pre_word == key:  
            continue  
        if counter[key] == 0:  
            continue
            
        counter[key] -= 1  
        dfs(key, length+1)  
        counter[key] += 1  

S = list(input().strip())  
counter = dict()           #dict로 문자:개수 저장

for s in S:
    if s in counter:
        counter[s] += 1 
    else:      #맨 처음 들어갈 때 없어서 그냥 +1로 하면 안됨
        counter[s] = 1
result = 0
dfs('', 0)  
print(result)
