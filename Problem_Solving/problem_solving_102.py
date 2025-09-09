# WAP that will give us ODD and EVEN value
"""
num1 = int(input("Enter first number: "))

if num1 % 2 == 0:
    print("당신이 입력한 숫자는 {} 이므로 짝수 입니다.".format(num1))
else:
    print("당신이 입력한 숫자는 {} 이므로 홀수 입니다.".format(num1))
"""


print("############### FUnction Program ################")
def oddeven(num1):
    if num1 % 2 == 0:
        print("당신이 입력한 숫자는 {} 이므로 짝수 입니다.".format(num1))
    else:
        print("당신이 입력한 숫자는 {} 이므로 홀수 입니다.".format(num1))

num1 = int(input("Enter first number: "))

oddeven(num1)



