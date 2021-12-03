f=0
s=1
print("Fibonacci Series::",f,s,end="\t")
for i in range(1,10):
    t=f+s
    print(t,end="\t")
    f=s
    s=t