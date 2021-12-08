def perfect(num):
    s=0
    for i in range(1,num):
        if(num%i==0):
            s=s+i
    if(s==num):
        print("Number is perfect")
    else:
        print("Number is not perfect")

num=int(input("Enter the number:"))
perfect(num)
