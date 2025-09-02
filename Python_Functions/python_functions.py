#less code, group of statement repeatedly required then use
# 적은 코드, 반복적으로 필요한 문장 그룹은 다음을 사용합니다
# unit of that code known as function
# 함수로 알려진 코드의 단위
# in built function
# 내장 함수
# user defined function
# 사용자 정의 함수
# doc string
# 문서 문자열
# function parameter
# 함수 매개변수
# return statement # multiple return
# 반품 명세서 # 복수 반품
'''
a = 200
b = 20
add = print(a+b)
sub = print(a-b)
mul = print(a*b)

a = 50
b = 60
add = print(a+b)
sub = print(a-b)
mul = print(a*b)
div = print(a/b)
'''


'''
def cal(a, b):
    """doc string
    this function is used for
    calculator """
    print("the sum of number are ", (a + b))
    print("the sub of numbers are", a - b)
    print("the multiplication of numbers are", a * b)

cal(100, 20)
cal(200, 20)
'''



'''def cal(a, b):
    sum = a + b
    return print(sum)

cal(100, 20)
cal(200, 20)'''

def cal(a, b):
    sum = a + b
    sub = a - b
    return sum, sub
sum, sub = cal(100, 20)
# sum, sub = cal(200, 20)

print('sum is ', sum)
print('sub is ', sub)











