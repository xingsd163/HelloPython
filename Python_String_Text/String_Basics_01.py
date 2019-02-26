# http://www.cnblogs.com/wkslearner/p/5929588.html
# https://www.cnblogs.com/printN/p/6924077.html
# https://www.cnblogs.com/yujihaia/p/7468253.html


# Read the first entries of a list

list = [
    'a',
    'b',
    'c',
    'd'
]

first_two = list[0:2]

for i in first_two:
    print(i)

print("Print the length of the list")
print(list.__len__())

# print the length of a list
print(len(list))

# revert the list
list.reverse()

print("Print list in reverse order")
for i in list:
    print(i)

print("range test")
for i in range(len(list)):
    print(i)


list1=['1','2','3']
list2=[1,2,3]

# Compare two lists
if list1 == list2:
    print("They are same")
else:
    print("They are different")