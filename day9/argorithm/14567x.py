# 17:38


n,m = map(int, input().split())
sunsu = [[0,0]]
con = ['']

for i in range(m):
    fi ,la =map(int, input().split())
    sunsu.append([fi,la])
    con.append(0)
    
print(con)

sunsu.sort()
print(sunsu)
k=1
for k in range(n+1):
    for i,j in sunsu:
        if i==0:
            pass
        elif i == k:
            print(i,j)
            # con[j] = con[i]+1
print(con)

        

    
    
# for i, j in sunsu:
    


# for a,b in sunsu
    