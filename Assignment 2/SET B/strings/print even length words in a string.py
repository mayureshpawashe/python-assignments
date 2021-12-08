str=input("Enter the string:")
str=str.split(' ')
print(str)
print("Even length words::")
for i in str:
    if(len(i)%2==0):
        print(i)
