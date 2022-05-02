#
rows = int(input("Enter number of rows::"))
for i in range(0, rows + 2):
    for j in range(i):
        print("*", end=" ")

# 10
num = int(input("Enter any number::"))
f = 0
if num == 1 or num == 0:
    f = 1
for i in range(2, num):
    if num % 1 == 0:
        f = 1
if f == 1:
    print("it is not prime number")
else:
    print("it is a prime number")
