def solution(num):
    cnt =0
    while True:
        print(num)
        if num%2 ==0:
            num=num//2
            cnt+=1
        else:
            num =num*3+1
            cnt+=1
        if num ==1:
            answer =cnt
            braxk
        elif cnt==500:
            answer =-1
            break
    return answer

print(solution(16))