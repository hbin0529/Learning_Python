# reversing order of string
"""
str1 = "Gudqls is a Good boy"

output = str1[::-1] # reverse
print(output)
"""
################################
'''str1 = "Gudqls is a Good boy"

rev = reversed(str1)

output = ''.join(rev)

print(output)'''

##############################
str1 = "Gudqls" # 5

output = ''
length = len(str1)-1
print(str1[length])

while length >= 0:
    output = output+str1[length]
    length = length-1
    # print(output)
print(output)
















