import sys
input=sys.stdin.readline
n = int(input())
re =0
for i in range(n):
    re =re+ int(input())
print(re-n+1)