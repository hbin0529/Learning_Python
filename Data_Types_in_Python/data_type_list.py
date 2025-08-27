'''
print("########################## LIST DATA TYPE ############################")
list1 = [1, 2, 3, 4, 5, 'aviral']
print(list1)
print(list1[0])
print(list1[-1])
list1.append(50)
print(list1)
print(type(list1))

print("########################## TUPLE DATA TYPE ############################")
tuple1 = (1, 2, 3, 4, 5, 'aviral')
print(type(tuple1))
tuple2 = ()
print(tuple2)
print(type(tuple2))

print("########################## SET DATA TYPE ############################")
set1 = {1, 2, 3, 4, 5, 'aviral'}
print(set1)
print(type(set1))
set1.add(50)
print(set1)
set1.remove(2)
print(set1)
set1.remove('aviral')
print(set1)

print("########################## FROZEN SET DATA TYPE ############################")
set1 = {1, 2, 3, 4, 5, 3, 'aviral'}
frz = frozenset(set1)
print(type(frz))
print(frz)


print("########################## DICT DATA TYPE ############################")
dict1 = {1: 'aviral', 2: 'is', 3: True, 4: 123}
print(dict1)
dict1[2] = 'bingo'
print(dict1)
dict1[4] = 'False'
print(dict1)

print("########################## RANGE DATA TYPE ############################")
# range(10, 50, 3) : 10부터 시작 ~ 50까지 3씩 증가
range1 = range(10, 50, 2)
print(type(range1))
# print(id(range1))
print(range1)
for x in range1:
    print(x)
'''

print("########################## BYTES and BYTE ARRAY DATA TYPE ############################")
list1 = [1, 2, 3, 4, 5]
byt = bytearray(list1)
print(type(byt))
print(byt)
byt = bytes(list1)
print(type(byt))
print(byt)










