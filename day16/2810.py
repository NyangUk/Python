n = int(input())
m = input()
m =m.replace('S','*')
m=m.replace('LL','*')
ans =len(m)+1
if ans >n:
    print(n)
else:
    print(ans)
