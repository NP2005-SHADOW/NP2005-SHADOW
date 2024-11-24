import math
n=0
k=6
for i in range(0,7):
    r=0
    print(" "*k,end="")
    while n<=i and r<n+1:
        print((math.comb(n,r)),end=" ")
        r=r+1
    k=k-1
    print()
    n=n+1
