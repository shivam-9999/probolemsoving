import math
n=int(input())
list1=[]
list1=list(map(int,input().split()))
max1=-math.inf
for i in range(n):
    lastI,sum1=i,0
    for j in range(2,n):
        l=lastI
        lastI=lastI+j
        if(lastI>=n):
            break
    for k in range(i,l+1):
        sum1=sum1+list1[k]
    if(max1<sum1):
        max1=sum1
print(max1)