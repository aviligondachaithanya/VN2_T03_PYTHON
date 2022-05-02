'''
list=[20,12,34,56,23]
print(list[4])
print(list[2])
print(list[4]
'''
'''
x=[12,23,34,45,67,89,90]
print(x[0:5:5])
print(x[3:5:2])
'''
'''
print("-----string------")
name = "chaithanya"
print(name)
print("3rd index value : ",name[5] )
print("6th index value:" , name[6])
print("3th negative value index:",name[-3])
print("1st negative value index:", name[-1]
print(" get partial name : ", name[0:6])
'''
list=[100,121,143,'chaithu',(1,2,4),20.1,{12:1,13:34},[1,2,6],{1,2,3}]
print("list:",id(list))
print("3rd index value:",[list])
print("3rd index value :",id(list[3]))
print("3rd index value:",(list[3][5]))
print("7th index value:",(list[7][2]))
print("6th index value:",(list[6]))

tuple=(100,121,143,'chaithu',(1,2,4),20.1,{12:1,13:34},[1,2,6],{1,2,3})
print("tuple:",tuple)
print("3rd index value:", (tuple)[3])
print("3rd index value:", (tuple[3][3]))
print("4th negative index value:",(tuple[-4]))
print("3rd negative index value:",(tuple[-3]))
print("3rd negative index value:",(tuple[-3]))

a=10
a+=5
print(a)
a=10
a_=5
print(a)

a=15
a/=10
print(a)

a=20
a*=5
print(a)

a=13
a//=4
print(a)


x=10
print(x)
print(type(x))
print(id(x))
'''
x=10-5*6/4+(4*9)+12
print(x)
print(id(x))
print(type(x))
 '''
'''
is_active=true
print("type of is_active:", type (is_active))
print("ID of is_active:", id(is_active)) '''

'''
a=10.2
print(bool(a))
print(int(a))
'''
'''
x=10
print(float(x))
print(bool(x))
print(type(x))
print(id(x))

'''

'''
y=14
x=13
print(y,id(y),bool(y),float(y))
print(id(x),float(x),int(x), id(y),float(y),int(y))
'''


c=13
print(c,id(c),type(c))

u='chay'
print(u,id(u),type(u))

x = 2j
print(type(x))
print(x)

x=2j
y=3j
z=4j
print(x+y+z)
print(x)
print(x*y*z)

x='sony'
print(x)
print(x,(3))

L=("chay","python")
print(L,id(L),type(L))

T={12, 1, 56, 78, 98}
print(T)

Z={"CHAY" : "mahesh", "VN" :22}
print(Z)


brand = {"model": "benz",
        "year": "2022",
        "price": "fiftyfive l"
        }
print(brand)
print(type(brand),id(brand))

chay= frozenset({"chaithayna","aviligonda","chay"})
print(chay)

x= frozenset({1,2,3,4,45})
print(x)


x = range(8)
print(x)

x = b"hello"
print(id(x),type(x))

chay = bytearray(99)
print(chay)

chay = memoryview(bytes(99))
print(chay)

chay = b"aviligonda"
print(chay)

x = str("aviligonda")
print((x),id(x), type(x))

_chay = str ('''haii 
how are you iam fine what about you''')
print((_chay), id(_chay), type(_chay))


h = str(99)
print(h)
print(id(h))

h = float(99)
print(type(h), id(h))

h = str(99.99)
print((h),id(h), type(h))

h = 99.00
print((h), id(h), type(h))

h = float(99.00)
print((h),id(h), type(h))

h = complex(9j)
print((h), id(h), type(h))






























