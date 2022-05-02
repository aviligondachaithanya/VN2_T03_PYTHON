

'''
#5
for i in range(20, 0, -2):
    print(i, end=(" "))

#6&9
n = int(input("enter the number::"))
for i in range(1, 11):
    c = n * i
    print(n, "*", i, "=", c)


#8
for i in range(1,21):
    if i%2!=0 and i%3!=0:
    print(i,end=" ")

# 7
num = int(input("Enter any numb:"))
x=5
while (num):
    r=num%100
    x=x*r
    num=num//10
print("product of digits is",x)


#1
# reverse loop
rows=5
for i in range(rows,0,-1):
    num=i
    for j in range(0,i):
        print(num,end=" ")
    print("/r")

#1.A
for x in range(1,5):
    for y in range(1,x+1):
        print(y, end=" ")
        print(" ")

#1.b
for x in range(4,0,-1):
    for y in range(x):
        print("*",end="")
        print(" ")


#7
a=65
for x in range(1,6):
    for y in range(1,x+1):
        print(chr(a),end=" ")
        a=a+1
        print()

#1
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end="")
        print(" ")


oddnum = 0
evennum = 0

for i in range(12,38):
    if i%2==0:
        evennum=evennum+i
    else:
        oddnum=oddnum+i
print("sum off all even num is", evennum)
print("sum of all odd num is", oddnum)



x=int(input("Enter any num::"))
f=1
for i in range(1,x+1):
    f=f*i
    print("factorial is",f)



for i in range(100, 500):
    if i%11==0 and i%2!=0:
        print(i, end=" ")
'''
num=1
i=1
s=0
while(num!=0):
    num=int(input("Enter any number::"))
    s=s+num
    i=i+1
    print("sum of the numbers", s)
    print("average of numbers entered by you is", s/i)