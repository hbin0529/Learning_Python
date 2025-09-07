# *args and **kwargs
# *args 는 연속되는 포지셔널 아규먼트를 다 먹는다.
# **kwargs 는 연속되는 키워드 아규먼트를 다 먹는다.
# *args 와 **kwargs 는 순서를 바꾸면 안된다.
# *args : 여러개의 인자를 받을 때 사용 *가 여러개의 인자를 묶어서 하나의 튜플로 만들어주고 이를 args에 할당한다.
'''def f1(*args): # 튜플
    print(args)
    print(type(args))

f1()
f1(10, 20, 30, 40, 50, 60)

# **kwargs : 여러개의 args들을 묶서 하나의 딕셔너리로 만들어준다.
def f2(**kwargs): # 딕셔너리 형태로 만들어줌
    print(kwargs)
    print(type(kwargs))

f2()
f2(a = 10, b = 2, c = 0, d = 1, e = 2, f = 5, g = 10, h = 23, i = 20)'''

'''def f2(*args, **kwargs):
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))

f2()
f2(10, 2, 0, d = 1, e = 20, f = 40) # 10, 2, 0 까지는 *args가 tuple로 먹고, 그 뒤에 **kwargs가 전부 먹는다.'''


# Global and Local variable : 전역변수, 지역변수
# 파이썬은 전역 변수보다 지역 변수를 선호 한다.
'''a = 20 # 전역 변수

def f1():
    # global a
    a = 10  # 로컬 변수
    print(a)
f1()

def f2():
    print(a)
f2()'''


# Lambda Function
# 람다 함수
'''
s = lambda n:n*n
print(s(4))

s = lambda n, m:n+m
print(s(4, 9))

bigger = lambda a, b : a if a > b else b
print(bigger(1, 2))
'''

# without filter
'''
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def iseven(n):
    if n % 2 == 0:
        return True
    else:
        return False

lst2 = []
for n in lst:
    if iseven(n) == True:
        lst2.append(n)
print(lst2)
'''

#######2nd program for even with filter
'''
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def iseven(n):
    if n % 2 == 0:
        return True
    else:
        return False
lst2 = []
s = list(filter(iseven, lst))
print(s)
'''
'''
####### 3rd filter + lambda 방식
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
s = list(filter(lambda n: n % 2 == 0, lst))
print(s)
'''

'''
# list 컴프리헨션 방식
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
s = [n for n in lst if n % 2 == 0]
print(s)
'''
'''
#map
lst = [1, 2, 3, 4, 5, 6]
def sqr(n):
    return n * n
lst2 = list(map(sqr, lst))
print(lst2)

# map with lambda
lst = [1, 2, 3, 4, 5, 6]
lst2 = [1, 3, 5, 7, 9, 11]
lst3 = list(map(lambda n, m: n**m, lst, lst2)) # n을 받아 m 만큼 제곱
print(list(lst3))
'''

'''
# Reducer
from functools import reduce # 내장 함수가 아니라 받아와야함
lst = [1, 3, 5, 4, 7, 11, 123, 65]
result = reduce(lambda x, y: x + y, lst) # lst의 값을 ((((x+y)+y)+y)...+y)수행
print(result)
'''
# first 100 numbers sum n = n * (n + 1) / 2
from functools import reduce
result = reduce(lambda x, y: x + y, range(0, 101))
print(result)



