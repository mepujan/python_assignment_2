# Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?

names=[]
print("Id Before appending:",id(names))
id_before_append= id(names)

for _ in range(5):
    name_of_friends= input("Enter name: ")
    names.append(name_of_friends)

print("Id After appending",id(names))
id_after_append= id(names)

if id_after_append == id_before_append:
    print("Id hasnot changed")
else:
    print("Id has changed")
print("Before Sorting: ", names)
names.sort()
print('After aorting',names)
print("firt item= {} and second item is = {}".format(names[0],names[1]))