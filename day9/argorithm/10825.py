from sys import stdin, stdout
# input = stdin.readline
# print = stdout.write

s = []
for i in range(int(input())):
    n, k, e, m = map(str, input().split())
    s.append((-int(k), int(e), -int(m), n))
s.sort()
for k in s:
    print(k[-1])

