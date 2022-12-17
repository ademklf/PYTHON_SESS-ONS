a= list ()
print(a)
print(type(a))


list1= ["a", "b", "c", "a"]
list2= [1,2,3]
list1.extend(list2)

print(list1)

list1= ["a", "b", "c", "a"]
list2= [1,2,3]
list1.extend(list2)

usa = "washington"
new_zeland = "wellinghton"
my_set1 = set(usa)
my_set2= set(new_zeland)

print(my_set1.difference(my_set2))
print(my_set1.intersection(my_set2))
print(my_set1.union(my_set2))