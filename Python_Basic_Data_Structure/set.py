'''set1 = {}
print(type(set1)) # dict '''

# properties of set
'''set1 = {1, 2, 3, 4 , 5, 6, 5, 5, 5, 1, 2, 3, 4, 5, 4, 3, 3, 3, "hbin is good boy", 192.168}
print(set1)

print(set1[1:6])'''

# mutable
'''set1 = {1.1, 2, 3, 4 , 5, 6, 5, 5, 5, "U hoo ~ ", 2, 3, 4, 5, 4, 3, 3, 3, "ggazaas", 192.168}
print(set1)
set1.add(100)
print(set1)'''

# creation of set
'''l = [ 1, 2, 3, 5, 6, 6, 5, 5, 4, 2, 2, 3, 7]
s = set(l)
print(s)'''

# s = set(range(1, 12))
# print(s)

# s = set("hbin is Good")
# print(s)

# len(), add(), update()
'''s = {2, 1, 2, 3, 5, 6, 6, 5, 5, 4, 2, 2, 3, 7}
print(s)
print(len(s)) # 객체의 길이

s.add(1217)
print(s)
print(len(s))

# list, tuple, set, dict, string 만 가능
# s.update([123, 529, 25, 3456]) # int 값 적용 되지 않으므로 해당 항목을 목록으로 변환 s.update([])
# s.update("hbin")
# s1 = sorted(s)
print(s)'''

# remove(), discard(), pop()
'''
set1 = { 1, 2, 3, 4, 5, 6}
print(set1)
set1.remove(2) # 해당 인자 제거
print(set1)
'''
'''
set1 = { 1, 2, 3, 4, 5, 6}
print(set1)
set1.discard(100) # 해당 인자 제거. 단, 없는 값이여도 오류는 나지 않음
print(set1)
'''
'''
set1 = { 1, 2, 3, 4, 5, 6}
# print(set1)
set1.pop() 
print(set1)
'''
'''
set1 = { 1, 2, 3, 4, 5, 6}
print(set1)
set1.clear() # 모든 내용 제거
print(set1)
'''

# union, intersection, difference
'''
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = set1.union(set2)
print(set3)
'''
'''
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6}
set3 = set1.intersection(set2) # 공통
print(set3)
'''
'''
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6}
set3 = set1.difference(set2) # 차이점
print(set3)
'''

set1 = {1, 2, 3}
set2 = {4, 5, 6}
# set3 = set1.union(set2)
set3 = set1 & set2 # and
# set3 = set1|set2 # or
print(set3)










