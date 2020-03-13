color =[['black',0],['brown',1],['red',2],['orange',3],['yellow',4],['green',5],['blue',6],['violet',7],['grey',8],['white',9]]

f =input()
s =input()
x =input()
ans =0
for i,j in color:
    if i ==f:
        ans = j*10
for i,j in color:
    if i ==s:
        ans = ans+j
for i,j in color:
    if i ==x:
        ans = ans*(10**j)

print(ans)