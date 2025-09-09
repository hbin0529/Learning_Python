# WAP that will tell me that provided year is a leap year or not
# 올해가 윤년? 여부 파악

# if the number will % of 4 and 100 and 400 == 0 then it will be leap year

"""
4로 나누어 떨어지면 윤년 (year % 4 == 0)
4로 나누어 떨어지며, 100으로 나누어 떨어지면 평년 (year % 4 == 0 and year % 100 == 0)
4로 나누어 떨어지며, 100으로 나누어 떨어지면서 400으로 나누어지면 윤년 ((year % 4 == 0 and year % 100 == 0)) and (year % 400 == 0)
4로 나누어 떨어지며, 100으로 나누어 떨어지지만 400으로는 나누어지지 않으면 평년 (year % 4 == 0 and year % 100 == 0 and year % 400 != 0))
4로 나누어 떨어지며, 100으로 나누어 떨어지지 않으면 윤년 (year % 4 == 0 and year % 100 != 0)
4로 나누어 떨어지지 않으면 평년 (year % 4 != 0)
"""

"""
year = int(input("Enter year: "))

if ((year % 4 == 0) and (year % 100 == 0)) or (year % 400 == 0):
    print("입력하신 연도는 {} 이며, 윤년 입니다. ".format(year))
else:
    print("입력하신 연도는 {} 이며, 윤년이 아닙니다.".format(year))
"""

print("Inside function")

def leapyear(year):
    if ((year % 4 == 0) and (year % 100 == 0)) or (year % 400 == 0):
        print("입력하신 연도는 {} 이며, 윤년 입니다. ".format(year))
    else:
        print("입력하신 연도는 {} 이며, 윤년이 아닙니다.".format(year))

year = int(input("Enter year: "))
leapyear(year)

















