# lstrip(), rstrip(), strip()

'''city = input("Enter City Name ").strip()
# lcity = city.lstrip() # 왼쪽 공간 제거
# rcity = city.rstrip() # 오른쪽 공간 제거
# strip_city = city.strip() # 양쪽 공간 제거
if city == 'Seoul':
    print("your choice is Seoul")
elif city == 'New York':
    print("your choice is New York")
elif city == 'Pune':
    print("your choice is Pune")
else:
    print("given city is not available")'''


# find(), rfind(), index(), rindex()
'''str = 'ABCBCAABCABCA'
find_str = str.find('BCAA')
print('provided substring is at {} index'.format(find_str))'''

'''str = 'ABCBCAABCABCA'
find_str = str.rfind('ABC')
print('provided substring is at {} index'.format(find_str))'''

'''str = 'ABCBCAABCABC'
find_str = str.index('ABCA') # 왼쪽 기준으로 해당 문자의 인덱스를 반환
print('provided substring is at {} index'.format(find_str))'''

'''str = 'ABCBCAABCABC'
find_str = str.rindex('A') # 오른쪽 기준으로 해당 문자의 인덱스를 반환
print('provided substring is at {} index'.format(find_str))'''


# count(), replace(), join(), split()
'''str = 'ABCBCAABCABC'
find_str = str.count('AB')
print(find_str)'''

'''str = 'ABCBCAABCABC'
find_str = str.replace('AB', 'SD')
print(find_str)'''

'''somevalue = 'hbin is good programmer'
split = somevalue.split()
for x in split:
    print(x)'''

somevalue = 'hbin is good programmer'
split = somevalue.split()
print(split)

join = ''.join(split) # spe.word
print(join)
join2 = '-'.join(split) # spe.word
print(join2)
join3 = '2'.join(split) # spe.word
print(join3)




















