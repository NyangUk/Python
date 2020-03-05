# 이진탐색
w = int(input())
n = list(map(int, input().split()))
n.sort()
print(w,n)

start ,end = 0,max(n)
mid = (start+end)/2

while start<end:
    mid = (start+end)//2 # 소수점 버리기
    if mid>w:
        start =1+mid
    else:
        end = mid-1
    print(mid)
    
print(mid)

