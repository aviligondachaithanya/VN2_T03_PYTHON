x = "chaithanya"
print(x)
print("3rd index value::", x[3])
print("5th index value::", x[5])
print("-2nd index value:", x[-2])
print("-4th index value:", x[-4])

list1 = [110, 23.5, True, 'Madhu', [1,2,3], (1,2), {1:10,2:20}, {1,2,3}]
print(list1)
print("List1:", id(list1))
print("list1:", type(list1))
print("3rd index value of list1:", list1[3])
print("5th index value of list1:", list1[5])
print("6th index value of list1:", list1[6])
print("7th index value of x:", list1[7])
print("1st index value of list1:", list1[1])



e_data = {'eid': 100,
          'name': 'MadhuNettem',
          'sal': 15000,
          'loc': 'Bangalore',
          'gender': 'Male'
          }
print(e_data)
print("dict data:", e_data["name"])
print("dict data:", e_data["sal"])
print("dict data:", e_data["gender"])
print("dict data:", e_data["loc"])


set1 = {11, 12, 13, 14, 15, 16, 17, 18}
print(set1, type(set1), id(set1))

x = 100
y = 200
print(x+y)

emp_ids = [100, 101, 102, 103, 104, 105]
print(emp_ids)
print(type(emp_ids))
print("2nd index value of emp_ids:", emp_ids[2])
print("4th index value of emp_ids:", emp_ids[4])
print("5th index value of x:", emp_ids[5])


x=100
print(x, type(x), id(x))
print(float(x))
print(bool(x))

x=23.23
print(x, type(x), id(x))
print(int(x))
print(x)
print(bool(x))

