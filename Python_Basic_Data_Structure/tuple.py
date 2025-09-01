# 일부 객체 그룹을 단일 엔티티로 표현 하려고 할때 설정
'''t1 = ()
print(type(t1))

t2 = (1, 2, 3, "hbin", 12.5, 'asd')
print(t2)
print(t2[4])
print(t2[0:3])

t2[1] = 56
print(t2)'''
from itertools import count

# single valued tuple
'''t3 = 1,
print(t3)
print(type(t3))'''

# creation of tuple
'''t4 = (1, 2, 3, 6)
print(t4)

# l1 = [1, 2, 3, 6 , 5]
l1 = 'hbin is good'
t = tuple(l1)
print(t)
print(type(t))

for item in t:
    print(item)
'''

'''r = tuple(range(2, 8))
print(r)

t = tuple('hbin is good')
print(t[0:2])
'''
'''# len(), count, reversed, sorted, index
r = (2, 3, 4, 3, 5, 8, 9, 10)
print(r)
# print(len(r))
# print(r.count(2))
# print(r.index(8))
# print(reversed(r))
# rev = reversed(r)
rev = sorted(r)
print(rev)
tuple1 = tuple(reversed(r))
print(tuple1)'''






