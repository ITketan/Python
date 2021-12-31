#python program to demonstrate creation of tuple
#creating an empty tuple
tuple1 = ()
print("initial empty tuple: ")
print(tuple1)

#creating tuple with the use of strings
tuple2 = ('python','for','programmers')
print("\nTuple with the use of string:")
print(tuple2)

#creting a tuple with the use of list
list1 = [1,2,3,4,5,6]
print("\nTuple using list")
print(tuple(list1))

#creating a tuple with the use of built-in function
tuple1 = tuple('king')
print("\nTuple with the use of function:")
print(tuple1)

#creating a tuple with neseted tuples
tuple1 = (0,1,2,3)
tuple2 = ('python','king')
tuple3 = (tuple1,tuple2)
print("\nTuple with nested tuples:")
print(tuple3)



