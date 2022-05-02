x = -10
y = 4


print("+++++++++++Arthemetic Operator+++++++++++++++++")
print(x + y)
print(x - y)
print(x * y)
print(x/y)  # returns exact quotient
print(x % y) # returns remainder
print(x ** y) # returns  power of  (-10)  to 4
print(x // y) # returns rounded quotient

print("========Relational operator======")
x = 100
y = 110


print(x == y)  # comparing values
print(x != y)   # Not equals
print(x > y)   #Greater than
print(x < y)  # lesser than
print(x >= y) # Greater than or equals to
print("after perform lessthan or equals:", x <= y)  # Lesser than or equals to

print("Assignment operators")

x = 10  # assign operator
y = 20
print(y)
# y+=x
y = y + x  # +=
print("Assigning y value after sum: ",y)


y = 10
print(id(x), id(y), type(x))

'''
x = int(input("Enter first number:"))
y = int(input("Enter seconf number:"))

result = x + y

print("End output:", result)
'''

print(x==y)  # comparing values
print(x is not y) # comparing memory locations

x = [10, 10, 20, 15]

print(id(x), id(x[0]), id(x[1]))


'''
# - for single line commenting
"""  
for using multine line
"""
'''



a = -1  # 1 represent True,  0 represent False
b = 1


print("Logical operator:", True and True)



y = ["x", 'a', 'm'] # x - variable, 'x' - string
print("checking memebership:", 'x' not in y)
print("checking memebership:", 'n' not in y)


x = 10
print(x, id(x))
y = 10
print(y, id(y))

print(x == y)  # comparing values
print(x is y)   # comparing address/ memory locations


x = 10  # address assined
del x