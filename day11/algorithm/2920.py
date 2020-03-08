asc ='12345678'
des ='87654321'

li =list(input().split())

re =''.join(li)

if re==asc:
    print('ascending')
elif re==des:
    print('descending')
else:
    print('mixed')