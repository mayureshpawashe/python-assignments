

def sum_lst(list1):
    sumoflist=sum(list1)
    print("Sum of list:",sumoflist)

n=int(input("Enter the limit:"))
list1=[]
print("Enter the list elements:")
for i in range(0,n):
    e=int(input())
    list1.append(e)
print("Original list:::",list1)
sum_lst(list1)