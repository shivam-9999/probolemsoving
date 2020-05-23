n,k = list(map(int,input().split()))
A = list(map(int,input().split()))
lis=[]
N=1000001
lis[:N+1]=[0]*(N+1)
for i in range(n):
    lis[A[i]]+=1
left=0
right=N
flag=0
while(left<right):
    if(lis[left]==0 or lis[right]==0):
        while(lis[left]==0):
            left+=1
        while(lis[right]==0):
            right-=1
    if((left+right)==k and left !=right ):
        flag=1
        break
    elif((left+right)<k):
        left+=1
    else:
        right-=1
if(left+right==k and left==right and lis[left]>1):
    flag=1
if(flag==1):
    print("YES")
else:
    print("NO")

