#program to implement list, tuple, dictionary operations
mylist1=[1,2,3,4,5]
mylist2=[6,7,8,9,10]
mytuple=("User1","User2","User3")
mydict={
    "C":1,
    "C++":2,
    "Python":3,
    "Java":4
}
print("1.LIST OPERATIONS")
print("  List 1:",mylist1)
print("  List 2:",mylist2)
mylist1=mylist1+mylist2
del mylist2
print("  Deleted List 2")
print("  List 1 after concatenation:",mylist1)
print("  Length of List 1:",len(mylist1))
print("  Retreiving the index of '5' from the concatenated list:",mylist1.index(5))
mylist1.remove(10)
print("  Removing 10 from list 1:",mylist1)
mylist1.append(0)
print("  Appending 0 to list 1:",mylist1)
mylist1.sort()
print("  Sorted List:",mylist1)
print()
print("2.TUPLE ACCESS")
print("  Tuple:",mytuple)
for i in mytuple:
    print(" ",i)
print("  Tuple Size:",len(mytuple))
print()
print("3.DICTIONARY DELETION")
print("  Dictionary:",mydict)
print("  Value of C++:",mydict["C++"])
print("  Removing key value pair of Python...")
mydict.pop("Python")
print("  Dictionary after deleting Python :",mydict)
