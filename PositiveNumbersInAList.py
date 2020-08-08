#program to print all positive numbers in a range
n= int(input("Enter the size of the list:"))
list1=[]
for i in range(0,n):
    p=int(input())
    if(p>0):
        list1.append(p)
print(list1)
    
