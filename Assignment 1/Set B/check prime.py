number=int(input("Enter The Number"))

if number>1:
    for i in range(2,int(number/2)+1):
        if (number%i==0):
            print( "is not a Prime Number")
            break
    else:
        print("is a Prime number")

else:
    print("is not a Prime number")