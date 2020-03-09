import sys

input=sys.stdin.readline
n = int(input())

cmd =['push','top','size','empty','pop']
stack =[]
for i in range(n):
    s = list(input().split())
    if s[0] == cmd[0]:
        stack.append(s[1])
    elif s[0] == cmd[1]:
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    elif s[0] == cmd[2]:
        print(len(stack))
    elif s[0] == cmd[3]:
        if len(stack) ==0:
            print(1)
        else:
            print(0)
    elif s[0] ==cmd[4]:
        if len(stack) ==0:
            print(-1)
        else:
            print(stack.pop())
    else:
        pass


    

                


