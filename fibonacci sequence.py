N=int(input("enter max limit:"))
a=0
b=1
x=a+b
print(a,end=",")
while(x<=N):
    print(x,end=",")
    x=a+b
    a=b
    b=x