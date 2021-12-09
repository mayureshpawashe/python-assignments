#SET-A  Write a python program to find the max of three numbers.

def max(a,b,c):
    if(a>b and a>c):
        print("A is MAXIMUM=",a)
    elif(b>a and b>c):
        print("B is MAXIMUM=",b)
    else:
        print("C is MAXIMUM=",c)

a=int(input("Enter the 1st no:"))
b=int(input("Enter the 2nd no:"))
c=int(input("Enter the 3rd no:"))
max(a,b,c)