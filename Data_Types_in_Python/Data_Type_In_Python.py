a = 10
b = 20

print('type :', type(a), 'id : ', id(a))
print("######################")

### Conversion
a = 0b111
print(a)
print("######################")

# Octal zero + O
a = 0O1234
print(a)

print("######################")

# HEXA
a = 0xface123
print(a)

print("######################FLOAT DATA TYPE #######################")
f = 1.3
print(type(f))

f = 12.456
print(f)
print("######################")

f = 1.2e3
print(f)

# By value can take lesser space
f = 1200000000000000000000000.00
print(f)
f = 1.2e+16
print(f)

print("###################### COMPLEX DATA TYPE ########################")

complex = 2+3j
print(complex)
print(complex.imag)
print(complex.real)

print("###################### Bool DATA TYPE ########################")

a = True
print(type(a))

print(True + True)
print(True + False)

print("###################### STRING DATA TYPE ########################")
a = "aviral"
print(a)
print(type(a))

s = 'aviral, str1, str2, str3'
print(s[0])

# print(s[100])

print("###################### Slicing DATA TYPE ########################")

print(s[-1])

print(s[:])










