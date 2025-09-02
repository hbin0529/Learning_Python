# Type of Argument
# Positional Argument, Keyword Argument, Default Argument, Variable Length Argument

'''def addition(a, b):
    print(a + b)

addition(1, 2) # 위치 논쟁'''

# Keyword Argument
'''def addition(a, b):
    print(a + b)

addition(a = 10, b = 20)
addition(b = 10, a = 20)
addition(10, b = 20)
addition(a = 10, 20) # Keyword Argument 오류'''


# Default Argument
'''def addition(a = 10, b = 20):
    print(a + b)

addition(a = 100, b = 20)
addition() # default argument'''


# Variable Length Argument
'''def sum(*n):
    print(type(n))
    print(n)

sum()
sum(10, 20)
sum(10, 20, 30)'''

'''def sum(*n):
    total = 0
    for x in n:
        total = total + x
        print("the sum of the VLA is ", total)

sum(1)
sum(10, 20)
sum(10, 20, 30)'''







