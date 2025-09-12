# palindrome 회문
str = input("Enter string: ")
# print(str)
# print(type(str))

if str == str[::-1]:
    print("완벽해! 이건 회문이에요!")
else:
    print("이건 회문이 아닌데요?? 다시 해봐요")
