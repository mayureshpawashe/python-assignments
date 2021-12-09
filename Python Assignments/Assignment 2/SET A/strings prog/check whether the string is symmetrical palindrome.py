
str=input("Enter the string::")
for i in range(int(len(str))):
    if(str[i]!=str[len(str)-i-1]):
        print("String is not palindrome")
        break
    else:
        print("String is palindrome")
        break

