# s1 = "abcabc"

# dic ={}# 중복 알파벳을 알아보기위함

# #모든 문자열을 검사할거임
# # i 번째 문자열이 중복이 안될경우 
# for i 
# s1 = "abcabc"
#     # 012345
#스타트를 갱신해줘야 할 때가 중복된 문자가 나왔을때!!
def get_len_of_str(s):
    if len(s) == 0:      # 문자열의 길이가 0일때 0을 리턴.
        return 0

    dic = {}        # 중복되지 않는 문자열과 그 인덱스를 딕셔너리에 추가
    max_length = start = 0  # 최대길이와 스타트 인덱스는 0에서 시작
    # sitting
    for i in range(len(s)):
        print(dic)
        if s[i] in dic and start <= dic[s[i]]:   #중복 문자열이 이미 딕셔너리에 존재하며, 스타트 인덱스가 중복 문자열의 인덱스보다 작거나 같은 경우, (abcabc에서 두번째 a가 등장했을때)
            start = dic[s[i]] + 1   # 스타트 인덱스 위치를 최초 중복 문자열의 인덱스에 1을 더하여 slide 시킴 (abcabc의 경우, a가 아니라 b 부터 길이를 재도록, 중복 문자열이 나올때마다 최초 중복 문자열을 제외하고 다시 카운트가 시작되도록 )
        else:  # 중복 문자열이 딕셔너리에 존재하지 않는 경우,
            max_length = max(max_length, i - start + 1) # 최대 길이는, 현재 최대 길이와 현재 문자열의 인덱스에서 스타트 인덱스를 뺀 문자열의 길이(길이를 구하므로 1을더해줌) 둘 중에 max값으로 지정.
        dic[s[i]] = i     # 해당 요소의 철자를 key, 인덱스 값을 value로 하여 dic 딕셔너리에 추가.

    return (max_length)

print(get_len_of_str("setting"))