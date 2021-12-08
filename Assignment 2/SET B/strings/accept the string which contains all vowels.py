str=input("Enter the string:")
vowels=['A','E','I','O','U','a','e','i','o','u']
for i in vowels:
    if(i not in str):
        print(f"{str} not accepted")
        break
    else:
        print(f"{str} accepted")
        break

