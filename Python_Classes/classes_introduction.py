# important terms
from pandas.io.formats.style import properties_args


# Classes
# Object
# Reference Variable
'''
class ClassName:

    """예시 클래스 # doc String"""
    variable = properties/attribute
    method/definication/functions
'''

"""
class Student:
    '''this class is about students'''

print(Student.__doc__)
help(Student)
"""
"""
class Student:
    ''' this is about your clas details'''

    def __init__(self):
        self.name = "hbin"
        self.age = 30
        self.classes = 12

    def talk(self):
        print('hello! I am a', self.name)
        print('My age is', self.age)
        print('My class is ', self.classes)

s = Student()
print(s.name)
print(s.age)
print(s.classes)
s.talk()
"""

class zenonia:
    def __init__(self, name, classes, weapon):
        self.name = name
        self.classes = classes
        self.weapon = weapon

    def intro(self):
        print('This game is Zenonia')


Lu = zenonia('루', '전사', '대검')


print('내 이름은', Lu.name)
print('나의 직업은', Lu.classes, '입니다')
print('내가 주로 사용하는 무기는', Lu.weapon, '이다')



