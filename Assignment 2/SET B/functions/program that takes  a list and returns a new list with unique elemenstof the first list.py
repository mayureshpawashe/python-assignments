def unique_lst(lst):
    x=[]
    for i in lst:
        if i not in x:
            x.append(i)
    print("Unique Elements:",x)

lst=[]
n=int(input("Enter the limit:"))
print("Enter the list elements:")
for i in range(n):
    ele=int(input())
    lst.append(ele)
print("Original list:",lst)
unique_lst(lst)

