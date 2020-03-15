def solution(heights):
    h =heights
    answer = [0]*len(h)
    for i in range(len(h)-1,-1,-1):
        for j in range(i-1,-1,-1):
            print(h[j],h[i])
            if h[j]>h[i]:
                answer[i]=j+1
                print(answer)
                break
    # print(answer)

    # answer.reverse()
        
    
    return answer


