# List
'''
lst = []
print(type(lst))
print(lst)
lst.append(10)
lst.append('hbin')
lst.append(192.16)
lst.append(10)
print(lst)

lst[3] = 123.12
print(lst)
lst[1] = 123
print(lst)

lst.remove(10)
print(lst)
# Hetro, insersetion, reamins, mutabil, duplicate
'''
'''
l = list("hbin is good")
print(l)

l2 = list(range(10, 20, 2)) # 10부터 20 미만까지 2씩 증가
print(l2)'''
'''
str = "Hbin is GOod"
l = str.split()
print(l)
'''
'''
str = "hbin is Good"
str2 = str.split()
print(str2[2])

print(str2[0:2]) # begin:n-1
print(str2[0:2:2]) # begin:n-1:2
'''

'''l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2'''

'''l1 = [1, 2, 3]
l2 = l1 * 2
print(l2)'''

'''
l1 = [10, 2, 3]
l2 = [4, 5, 6]
l3 = [3, 2, 10]
l4 = [3, 2, 10]

print(l4 == l3)
print(l4[2] < l2[0]) # 인덱스를 줌으로써 자리에 따른 비교
print(l4 < l2) # 첫번째 인덱스 비교
'''

# len() count() index()
'''
l1 = [1,2,3,4,5,6,2,1,4,5,7,87,15]
print(len(l1))
print(l1)
print(l1.count(14))

print(l1.index(3))
'''
'''
# append(), insert()
l2 = [1,2,3, 6, 5, 3]
l2.append(7)
print(l2)
l2.insert(2, 8) # insert(index, obj)
print(l2)
l2.__delitem__(-1) # __delitem__(index)
print(l2)
l2[1] = 75
print(l2)'''

'''
# extend() and Append()
l1 = [10, 2, 3]
l2 = [4, 5, 6]
l1.append(l2)
print(l1)
# l1.extend(l2)
# print(l1)
'''

# pop(), clear(), reverse(),reversed(), sort(), sorted()

'''
l1 = [10, 2, 3, 10]
print(l1)
l1.pop()
print(l1)
l1.pop()
print(l1)
l1.pop()
print(l1)
l1.pop()
print(l1)
l1.pop()
print(l1)
'''
'''l1 = [10, 2, 3, 10]
print(l1)
l1.clear() # 전체 비우기
print(l1)'''

'''l1 = [10, 2, 3, 10]
print(l1)
l1.reverse()
print(l1)'''

'''l1 = [10, 2, 3, 10]
print(l1)
l1.sort()
print(l1)'''

'''l1 = [10, 2, 3, 10]
print(l1)
l1.sort() # 오름차순 정렬
print(l1)
l1.sort(reverse=True) # 내림차순 정렬
print(l1)'''

l1 = [10, 2, 3, 9, 12, 11, 36]
print(l1)
l2 = sorted(l1)
print(l2)
print(type(l2))







# tuple, set, dict















