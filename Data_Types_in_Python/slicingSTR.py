string3 = 'aviral'
string4 = string3[0].upper()+string3[1:]
print(string4) # Aviral
print(string4[0].lower()+string4[1:]) # aviral
print(string4[0].lower()+string4[:1]) # aA
# print(string3[0].upper()string3[1:])

print("##############################################")

string5 = 'aviralisagoolboy'
print(string5[0].upper()+string5[1:len(string5)-1]+string5[-1].upper())


print("##############################################")

floattoint = int(12.3)
print(floattoint)

inttofloat = float(12)
print(inttofloat)

# complex = complex(12.3)
# print(complex)

complexconversion = complex(2, 6)
print(complexconversion)

print("##############################################")

first1 = 10
first2=first1+1

print(first1, first2)
print(id(first1), id(first2))

av = 10
bd = 11

print(id(av), id(bd))






