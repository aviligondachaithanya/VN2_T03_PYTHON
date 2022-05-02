'''
num=1
count=0
while num<100:
    if num % 2 == 0:
        print(num,end=" ")
        count += 1
    if count == 7:
        break
    num += 1
print("End of the loop")


num=1
count=0
while num<100:
    if num % 3 == 0:
        print(num, end=" ")
        count += 1
        if count == 20:
            break
    num += 1
print("End of the loop")
num=1
count=0
while num<120:
    if num % 4 ==0:
        print(num, end=" ")
        count +=1
        if count == 5:
            break
    num +=1
print("End for the loop")

num=1
count=0
while num<100:
    if num % 5 ==0:
        print(num,end=" ")
        count +=1
        if count == 10:
            break
    num +=1
print("End for the loop")

num=1
count=0
while num < 100:
    if num % 5 == 0:
        print(num, end=" ")
        count += 1
    if count == 10:
        break
print("End for the loop")

num=1
count=0
while num<100:
    if count>7:
        break
    if num % 3 == 0:
        print(num, end=" ")
        count += 1
    num += 1
print("Exited while loop")

num=1
count=0
for num in range (1,101):
    if num % 2==0:
        print(num, end=" ")
        count += 1
        if count == 7:
            break
print("End for the loop")

for i in range (50,80):
    if i>50 and i<=80:
        if i % 2==0:
            print(i,end=" ")
    elif i > 80:
        break
print("End for the loop")

for i in range(100,150):
    if i>100 and i<150:
        if i % 5==0:
            print(i,end=" ")
    elif i > 150:
        break
print("End for the loop")


i=500
count=0
while i<=1000:
    if i % 5 == 0:
        count += 1
        print(count, ":", i, end=" ")
        if count == 15:
            break
    i += 1


count=1
for i in range (500,1001):
    if i % 10 == 0:
        count += 1
        print(count, ":", i, end=" " )
        if count > 25:
            break
    i += 1

#continue statement
for i in range (1,100):
    if i % 5 ==0:
        if i % 10 ==0:
            continue
    print(i, end=" ")


count=100
for i in range(1,50):
    if i % 2 == 0:
        if count>3:
            break
        print(i, end="")
        count += 1
print("Both continue break")


count = 0
for i in range (1, 51):
    if i % 2 == 0:
        count += 1
        if count < = 4:
            continue
        print(i, end=" ")
        if count>7:
            break

count=0
list1 = [3, 5, 20, 6, 8, 2, 7, 3, 1, 6, 2, 6, 8, 4, 2]
for i in list1:
    if i % 2 == 0:
        print(i, end =" ")
        count += 1
        if count == 3:
            break
'''
# count = 0
list1 = [3, 5, 20, 6, 8, 2, 7, 3, 1, 6, 2, 6, 8, 4, 2]
for i in list1:
    if i / 2 != 0:
        print(i, end=" ")

































