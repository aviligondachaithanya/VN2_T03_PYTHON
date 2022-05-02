'''
# str = "python"
# for i in str:
#    print(i, end="")

str = "chaithu"
for x in str:
    print(x,end="")

list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in list:
    print(i, end=" ")

n = 5
for i in list:
    c = n*i
    print(c)

list = [10, 20, 30, 40, 50]
sum = 0
for i in list:
    sum = sum+i
    print("the sum is:", sum)

list = [ 'chay', 'vannur', 'vn2']
for i in list:
    print(i,end=" ")
for i in range (len(list)):
    print("hello",list[i])
'''

#x = "palle tech banglore"
#print(len(x)-1)
#i=0
#while i<=4:
 #   print(x[i],end="")
 #   i=i+1

#while i<=len(x)-1:
 #   print(x[i],end="")
  #  i=i+2


#( x[0+len(x)-1//2])
'''
x=[10, 11, 15, 25, 18]
i=0
while i<=4:
    if x[i]%5==0:
        print(x[i])
    i=i+1
 
  
x = [10, 11, 12, 15, 18, 19]
i=0
while i<=len(x)-1:
    if x[i]%3 ==0:
        print("even number")
else:
        print("odd number")
#    i=i+1

y=[12,23,45,48,64,32,12,18,24]
i=0
while i<=len(y)-1:
    if y[i] % 8==0:
        print(y[i])
    i=i+1

while True:
    if i<=5:
        print(i)
        i=i+1
    else:
        i=i-1
        
list = [10,30,23,43,65,12]
sum=0
for i in list:
    sum = sum+i
print("the sum is:", sum)

list = [12,34,56,78,88,12]
sum=0
for i in list:
    sum = sum+i
print("the sum is:", sum)


for i in range(100):
    print(i, end=" ")

n=int(input("Enter any number::"))
for i in range(1,11):
    c=n*i
    print(n, "*", i, "=", c)


n=int(input("Enter any number::"))
for i in range(1,16):
    c=n*i
    print(n, "*", i, "=", c)

n=int(input("Enter any number::"))
for i in range(0,51,2):
    print(i,end=" ")


rows=5
for i in range(1,rows+1):
    for j in range(i):
        print("*",end=" ")

rows=10
for i in range(1,rows+10):
    for j in range(i):
        print("x", end="")
    print()

rows=int(input("Enter any number::"))
for i in range (1,rows+6):
    for j in range(i):
        print(i, end=" ")
    print()

rows=int(input("Enter any number:::"))
for i in range(1,rows+5):
    for j in range(i):
        print(i,end=" ")
    print()


for i in range(0,5):
    print(i,end=" ")
    break;
'''

#for loop wit data structures
'''
course = 'PYTHON PROGRAMMING'
for i in course:
    print(i, end=" ")

msg = 'Python world '
for i in msg:
    print("charcters:", i)
print(msg)
print(msg[0])
print(msg[2])
print(msg[6])
print(msg[5])
print(msg[4])

for char in 'aflkdsfdsalfsdf  324324SDFDSF@!#@!$#@%fsdfsd dsfdsFDSf!@#@!#!@':
    print("char:" ,char)


list = [1, 2.5, True, 'Madhu', 5.0, False, 7]
for val in [1, 2.5, True, 'Madhu', 5.0, False, 7]:
    print("list data:", val)
print(list[2])
print(list[5])
print(list[3])
print(list[6])

tuple=(1, 2, 3, 4, 5, 6, 7)
for val in (1, 2, 3, 4, 5, 6, 7):
    print("tuple data:", tuple)
print(tuple[3])
print(tuple[5])


Dict={'eid': 100.50, 'name': 'Madhu Nettem', 'sal': True}

e_data = {'eid': 100.50, 'name': 'Madhu Nettem', 'sal': True}
print(e_data)
#for i in e_data:
#    print("Dict value:", "sal")
#    print("Dict value:", i)
#    print("e_data:", e_data)
# print("Dict data:", e_data)
#    print("Dict key:", i )
#    print("Dict key:", "name")


set1 = {1, 2, 3, 4, 5, 6}
print(set1)
for i in  set1:
    print("set data:", i)
#    print("set data:", set1)





# variables with loops
x=10
y=15
print(x+y)

val=10+20
print(val)
print(val+20)
print("addition is:", 10+20)

x=30
y=40
print("addition is:", x+y)
print("subtraction is:", x-y)
print("multiplication is:", x*y)
print("divison is:", x/y)


x=10
y=20
res=x+y
print("addition is:", res)
print("addition is:", 100+res)
print("subtraction is:", res-10)

x= "hello world"
# print(x)
for i in x:
    print("charcter:", i)
print(x[2])
print(x[5])
print(x[6])

# range
for i in range (0,10):
    print(i,end="")

for i in range (0,-10,-1):
    print(i,end="")

for i in range (0,-10,-2):
    print(i,end="")

for i in range (100,-100,-2):
    print(i,end=" , ")


#Dictonary

emp_details = {'eid': 100,
               'ename': 'MadhuN',
               'sal': 12500}
# print(emp_details)
#for i in emp_details.items():
#    print(i)

for i in emp_details.keys():
    print(i)

for i in emp_details.values():
    print(i)


set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i,end=" ")
    

str="python"
for i in str:
    print(i,end="")

list = [1,2,3,4,5,6,7,8,9,10]
list2 = [5, 10, 15, 12]
for i in list:
    for j in list2:
        c = i * j
        print(c, end=" ")


list = [10,30,23,43,65,12]
x=0
for i in list:
    x=x+i
print("sum of the num", x)

list = [1,2,3,4,5,6,7,8,9,10]
x=0
for i in list:
    x=x+i
print("the sum is", x


n=int(input("Enter any numb::"))
for i in range(1,11):
    c= n * i
    print(n, "*", "i", "=", c)


list = ['Peter','Joseph','Ricky','Devansh']
for i in range (len(list)):
    print("hello", list[i])

rows=5
for i in range(1,rows+5):
    for j in range (i):
        print(i,end=" ")
    print()


rows=9
for i in range(1,rows+9):
    for j in range(i):
        print(i,end=" ")
    print()


rows=-5
for i in range(-1,rows-5):
    for j in range(i):
        print(i, end=" ")
    print()


for i in range(0,5):
    print(i, end=(" "))
else:
    ("for loop completely exhausted, since there is no break.")
'
for i in range(0,5):
    print(i, end=" ")
    break
else:
    print("for loop is exhausted")
print("the loop is broken due to break statement....came out of the loop")


# basics

i = 1
while i < 101:
    pass

message = "Hello World"
for i in message:
    print(i, end=" ")
print("end for the loop")

number = "12345"
for i in number:
    print(i,end="")

list1 = [1, 2, 3, 4, 5]
for i in list1:
    print(i, end=" ")


list1 = [1, 2, 3, 4, 5]
for val in list1:
    print(val**2, end=" ")

for val in list1:
    print(val**3, end=" ")

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 10, 20, 30]
for val in list2:
    if val in list1:
        print("yes:", val)
    else:
        print("no:", val)
'''
count=0
for i in range(0,101):
    if i % 9 == 0:
        print(i, end=" ")
        count += 1
        if count == 4:
            break
print("end of the loop")




































