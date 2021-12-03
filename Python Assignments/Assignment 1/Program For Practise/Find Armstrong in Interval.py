a=int(input("Enter Starting Number::"))
b=int(input("Enter Ending Number::"))
for i in range(a,b):
    n=i
    s=0
    while(n>0):
        d=n%10
        n=int(n/10)
        s=s+(d*d*d)
    if(s==i):
        print(i)
