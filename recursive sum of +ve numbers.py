a=int(input("enter a +ve number:"))
b=int(input("enter a +ve number:"))
def sum(a,b):
    if a==0:
        return b
    else:
        return sum(a-1,b)+1
print(sum(a,b))