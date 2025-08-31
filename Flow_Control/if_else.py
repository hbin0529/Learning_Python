'''
print("Learning If Else selection statement")
for i in range(5):
    x = int(input("Enter Number "))
    if x == 10:
        print("your choice is 10")
    elif x == 20:
        print("your choice is 20")
    elif x == 30:
        print("your choice is 30")
    else:
        print("your choice number is not there")


weather = 'winter'
# if weather == "winter":
if weather == weather:
    print("dont forget to take jacket")
else:
    print("your choice is {}".format(weather))
'''
'''
print("Learning Iterative statement")
# for and while
# For we use for sequence but while we use for some condition

value = 'Gudqls dlqslek'
# value = [10, 20, 30, 40]
# value = (10, 20, 30, 40)
i = 0
for x in value:
    print("the char in {} index and teh value is {}".format(i, x))
    i = i + 1
'''

'''
for x in range(20):
    if x % 2 == 0:
        print(x)
'''

'''
print("while loop or statement")
i = 1
while i <= 10:
    print(i)
    i = i + 1
'''
'''
print("infinite loop")
i = 0
while True:
    print("hello", i)
    i = i + 1
'''
'''
print("Nested loop loop")
for x in range(3):
    for y in range(2):
        print("hello where x {} and y {}".format(x, y))
'''

'''
print("Transfer statement")
for i in range(10):
    if i == 6:
        print("break program")
        break # i 가 6이면 프로그램 종료
    print(i)
'''
'''
for i in range(10):
    if i == 6:
        print("break program")
        continue # i 가 6이면 프린트문 보내고 계속
    print(i)
'''

'''print("pass and del statement / keyboard")

def f1():
    pass


def f2():
    pass'''

'''print("del keyword")
x = 10
x1 = x
x2 = x1
print(x)

del x
print('x1의 값은 : ', x1, ', x2의 값은 :',  x2)'''



















