s ="[)"

flag =0
for i in range(len(s)//2):
    if s.find('(')>0:
        if s[s.index('(')+1]==')':
            flag = 1
        else:
            flag =0
    if s.find('{')>0:
        if s[s.index('{')+1]=='}':
            flag = 1
        else:
            flag =0
    if s.find('[')>0:
        if s[s.index('[')+1]==']':
            flag = 1
        else:
            flag =0
print(flag)