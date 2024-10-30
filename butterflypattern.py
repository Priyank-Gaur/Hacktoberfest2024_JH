for i in range(n-1):
    j=0
    while j<=i:
        print("*",end=" ")
        j+=1
    j=0
    while j<2*(n-i-1):
        print(" ",end=" ")
        j+=1
    j=0
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
for i in range(n):
    j=0
    while j<=n-i-1:
        print("*",end=" ")
        j+=1
    j=0
    while j<2*i:
        print(" ",end=" ")
        j+=1
    j=0
    while j<=n-i-1:
        print("*",end=" ")
        j+=1
    print()
