m,d = map(int,input().split())

month =[31,28,31,30,31,30,31,31,30,31,30,31]

def dis(day):
    c = day%7
    if c ==1:
        print('MON')
    elif c ==2:
        print('TUE')
    elif c ==3:
        print('WED')
    elif c ==4:
        print('THU')
    elif c ==5:
        print('FRI')
    elif c ==6:
        print('SAT')
    elif c ==0:
        print('SUN')


for i in range(m):
    day = sum(month[0:m-1])
    day += d

dis(day)

# m,d = map(int,input().split())

# month =[31,28,31,30,31,30,31,31,30,31,30,31]
# week =['SUN',MON TUE WED THU]
# for i in range(m):
#     day = sum(month[0:m-1])
#     day += d

# dis(day)



