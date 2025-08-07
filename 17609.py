

def is_palindrome(str):
    for left in range(len(str)):
        right = len(str) - left -1
        if str[left] != str[right]:
            return False
        if left >= right:
            return True
    
def is_pseudo(str):
    for left in range(len(str)):
        right = len(str) - left -1 
        if str[left] != str[right]:
            s1 = str[ :left] + str[left+1: ]
            s2 = str[ :right] + str[right+1: ]
            if is_palindrome(s1) or is_palindrome(s2):
                return True
            else:
                return False

def solve():    
    str = input().strip()
    if is_palindrome(str):
        print(0)
        return
        
    if is_pseudo(str):
        print(1)
        return
        
    print(2)
        

N = int(input())
for _ in range(N):
    solve()
    
    