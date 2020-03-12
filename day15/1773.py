# import sys
# input=sys.stdin.readline
# n,m =map(int,input().split())
# t =[]
# re = [0]*(m+1)
# for _ in range(n):
#     t.append(int(input()))

# for i in t:
#     for j in range(i,m+1,i):
#         re[j] = 1
# print(sum(re))

n,c=map(int,input().split())
t=[0]*(c+1)
for _ in range(n):
    i=int(input())
    for j in range(i,c+1,i):t[j]=1
print(sum(t))