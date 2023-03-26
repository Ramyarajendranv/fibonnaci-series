#fibonacci series
n=int(input("Enter the no of terms:"))
def f(n):
    if(n<=1):
        return(n)
    else:
        return(f(n-1)+f(n-2))
if(n<0):
    print("Enter the positive integer") 
else:
    for i in range(0,n):
        print(f(i))

#without using recursion        
a=0
b=1
for i in range(10):
    print(a)
    b,a=b,a+b'''





