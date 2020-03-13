def solution(s1):
    # abj
    c =['aa','bb','cc','ss','ee','ff','gg','hh','ii','jj','kk','ll','nn','mm','oo','pp','qq','rr','ss','tt','uu','vv','ww','xx','yy','zz']
    s =s1
    flag =0
    while True:
        s=list(s)
        for i in c:
            if i in ''.join(s):
                flag=1
                break
            else:
                flag =0
        print(flag)
        s=list(s)
        if flag ==1:
            for i in range(len(s)-1):
                if s[i] ==s[i+1]:
                    print(s[i],s[i+1])
                    del s[i:i+2]
                    break
        else:
            return 0
        print(s)
        if len(s)==0:
            return 1
        
print(solution('baabaa'))