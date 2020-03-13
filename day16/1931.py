n = int(input())
for _ in range(n):
    li =list(map(int,input().split()))
    re =li[1]-li[2]
    if li[0]<re:
        print("advertise")
    elif li[0]==re:
        print("does not matter")
    elif li[0]>re:
        print("do not advertise")
    
