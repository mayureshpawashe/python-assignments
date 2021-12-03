
year = int(input("Enter Year:"))

if year%4==0 and year%100!=0:
    print(" It is a Leap Year")
else:
    print("It is not Leap Year")