n= int(input())
cute=[]
for _ in range(n):
    cute.append(int(input()))
cnt0 =0
cnt1 =0
for k in cute:
    if k==1:
        cnt1+=1
    else:
        cnt0+=1

if cnt0>cnt1:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")

