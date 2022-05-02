import random

r = list(("WATER", "BOTTELE", "pour"))
print(r)
print(type(r))

s = list(("chay", "chaithanya", "aviligonda", 11, 112, 113))
print(s)
print(type(s))

d = set((11, 12, 13,14))
print(d)
print(type(d), id(d))

s = set(("chay", "anantapur", "atp"))
print(s)
print(id(s), type(s))

x = dict(brand="benz", model="generic")
print(x)


e = bytes(9)
print(e)
print(type(e))

x=23
y=-42
z=21
print(x, type(x))
print(y)
x="23"
print(x, type(x))


x = 22e4
print(x)

y = 4578e3
print(y, type(y), id(y))

x=7+8j
y=6j
z=-7
print((x), type(y))
print(x+y)
print(x+y+z)

print(random.randrange(1, 10))
print(random.randrange(1, 100))

chay_1=99
print(chay_1)
chay_2= 1
print(chay_1+chay_2)

chay_1 = "aviligonda"
print(chay_1[1:4])
print(chay_1[3:5])

chay_2 = "chaithanya"
print(chay_2)
print(chay_1 + chay_2)

print(chay_1[:10 ]+ "chay")

del(chay_1)


bro = ["chay", "chaithanya", "aviligonda"]
bro_1 = ["raj", "rajsekhar", "aviligonda"]
print(bro)
print(bro[2:5])
print(bro[1:3])
print([bro]+[bro_1])
print("3rd index value:", id(bro[1:4]))

chay = ["chay", "baba", (9,2,3), [12,14,16], "sairam"]
print(chay)
print("3rd index value :", id(chay[2]))
print("slice :",type(chay[1]))
print("slice:",chay[3])
print("slice:",chay[2][1])
print("slice:",chay[4][1:3])




chay = {"massy:vn" ,
      "python:it",
      "whitefiled:office"}
print(chay)
print("chay:",type(chay))
print("chay:", id(chay))


set={1,2,3,4,5,}
print(set)
print("set :", set)

















