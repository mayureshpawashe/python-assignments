

test=input("Enter the string:")
print("Original string:",test)
new=""
pos=int(input("Enter the position:"))
for i in range(len(test)):
    if(i!=pos):
        new=new+test[i]
print(" after removal the character:",new)