n = int(input())
s =[]
for _ in range(n):
    s.append(list(input()))

# 가로 찾기 
cnt =0
ans =0
for i in range(n):
    cnt =0
    for j in range(n):
        if s[i][j] =='.':
            cnt+=1
        elif s[i][j] =='X':
            if cnt>=2: #누울자리는 2개 이상이여야 함
                ans+=1
            cnt=0
    if cnt>=2:
        ans+=1
print(ans)
ans =0
for i in range(n):
    cnt =0
    for j in range(n):
        if s[j][i] =='.':
            cnt+=1
        elif s[j][i] =='X':
            if cnt>=2: #누울자리는 2개 이상이여야 함
                ans+=1
            cnt=0
    if cnt>=2:
        ans+=1

print(ans)