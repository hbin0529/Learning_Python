# Dictionary
'''dic = {1:["hbin", "love", "wlgP"], 2:"wlgP", 3: 12.5}
print(dic)
print(type(dic))

for item in dic:
    value = dic[item]
    if isinstance(value, list):
        for v in value:
            print(v)
    else:
        print(value)
    # print(dic[item])'''
from Tools.scripts.make_ctype import values

# key value pairs
# Duplicate Keys are not allowed, if there are dup then it will take last assigned value
# Hydro object allowed
# Values can be duplicated
# indexing and slicing is not allowed
# Mutable
# Dynamic

# Creation of Dict

'''d = {} # 기본 dict 문법
print(type(d))

# dict() 라고 선언해주면 type이 dict가 된다.
d = dict([(1, 2), (3, 4)]) # ()
print(d)
print(d.keys())
print(d.values())
print(type(d))'''

'''
dic = {1:"hbin", 2:"love", 3:"wlgP", 4: 12.5}
print(dic)
print(dic[2])
'''


# adding data
'''
dic = {1:"hbin", 2:"love", 3:"wlgP", 4: 12.5}
print(dic)
dic[3] = "wPWP"
print(dic)
dic[5] = "gudqls"
print(dic)
'''

'''
# operation
dic1 = {1:"hbin", 3:"wlgP"}
print(dic1.keys())
print(dic1.values())
dic2 = {1:"hbin", 3:"wlgP"}
# dic3 = dic1 + dic2 # dict + dict 불가 
# print(dic3)
print(dic1 == dic2) # 키와 값이 동일 해야 True, 순서는 상관없다 ex) {1:v, 3:v}, {3:v, 1:v} / 키와 값이 하나라도 동일하지 않다면 False 
'''

# checking value
'''dic1 = {1:"hbin", 3:"wlgP"}
print(1 in dic1) # Dictionary 안에 키의 번호가 있는지 있으면 True
print(3 in dic1) # 없으면 False
print(6 in dic1) #'''

# len(), get(), update()
'''dic1 = {1:"hbin", 3:"wlgP"}
print(len(dic1)) # 길이'''

# get
'''
dic1 = {1:"hbin", 3:"wlgP"}
print(dic1[1], dic1[3])
# print(dic1[2]) # for preventing error we use get function
print(dic1.get(3), "is pretty") # 키를 찾는다
print(dic1.get(100)) # 키를 찾을 때 없으면 None
print(dic1.get(100, "LOVE")) # dic.get(data, default)
'''

# update
'''dic1 = {1:"hbin", 3:"wlgP"}
dic2 = {1:"hbin2", 4:"wlgP"}
print(dic1)
dic1.update(dic2) # dic1에 dic2의 값을 뒤에 넣는다. 단, 키가 중복이면 하나만 나오되, 값이 다르다면 dic2의 값으로 변경된다 
print(dic1)'''

# keys, values, items
'''dic1 = {1:"hbin", 2:"wlgP", 3:"hhh", 4:"two"}
print(dic1.__getitem__(1))
print(dic1.values())
print(dic1.keys())
print("-=")
for keys in dic1:
    print(keys)
    print(dic1.values())'''

# items
'''dic1 = {1:"hbin", 2:"wlgP", 3:"hhh", 4:"two"}
for k, v in dic1.items():
    print(k, "----", v)'''

# pop, pop.item
'''dic1 = {1:"hbin", 2:"wlgP", 3:"hhh", 4:"two"}
print(dic1)
# print(dic1.pop(4))
print(dic1.popitem())
print(dic1)
print(dic1.popitem())
print(dic1)'''

# clear() 딕셔너리 키 값 모두 삭제
'''dic1 = {1:"hbin", 2:"wlgP", 3:"hhh", 4:"two"}
print(dic1)
print(dic1.clear()) # None
print(dic1)'''

# Setdefault : 이미 설정된 키에는 적용 안 됌.
dic1 = {1:"hbin", 2:"wlgP", 3:"hhh", 4:"two"}
print(dic1)
# dic1[1] = "HBIN"
# print(dic1)
dic1.setdefault(5, "HXXBIN") # 설정되어있는 키가 없다면 추가 가능
print(dic1)














