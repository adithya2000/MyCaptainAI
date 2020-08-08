fib=[0,1]
n= int(input("Enter the number until which the series has to be printed:"))
for x in range (2,n):
    fib.append(fib[-2]+fib[-1])
print(fib)
    
