i,j =map(int,input().split())
if i >j:
    i,j =j,i
elif i<j:
    pass

sum =(i-1)+(j-1)*i
print(sum)
