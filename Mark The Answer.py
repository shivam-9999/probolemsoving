n,k = list(map(int,input().split()))
A = list(map(int,input().split()))
t,index=0,0
if(n==1):
        index=n
for i in range(n):
    if(A[i]>k):
        t+=1
        if(t==2):
            index=i
            break
    else:
        pass
        if(t==0 and i==n-1):
            index=n+1
print(index-1)