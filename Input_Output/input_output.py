# a = eval(input("무엇이든 입력하세요 - "))
# print(a)
# print(type(a))

# a, b, c, d = [int(x) for x in input("Enter two numbers: ").split()]
# print(a + b + c + d)
# print(a * b)
# print(b * c)

from sys import argv
print(argv[0])
print(argv[1])
print(argv)
for x in argv:
    print(x)





