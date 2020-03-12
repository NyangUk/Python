# 6 9 5 7 4
def solution(heights):
    s = heights
    answer = []
    for i in range(len(s)-1,0,-1):
        re =0
        for j in range(i-1,-1,-1):
            if s[j]>s[i]:
                re = j+1
                break
            else:
                pass
        answer.append(re)
    answer.append(0)
    answer.reverse()
    return answer

