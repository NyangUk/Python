import itertools

name =[1,2,3]
# 숫자의 경우
print(list(itertools.permutations(name))) # 
print(list(itertools.permutations(name,2)))

print(list(itertools.combinations(name,1))) # 
print(list(itertools.combinations(name,2)))

# print(list(map(''.join,itertools.combinations(name))))