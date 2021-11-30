n=int(input("Enter Number ::"))
sum=0
n1=n
while(n>0):
    d=n1%10
    n1=int(n1/10)
    sum=sum+d*d*d
if(n==sum):
    print("Number Is Armstrong")
else:
    print("Number is not Armstrong")
