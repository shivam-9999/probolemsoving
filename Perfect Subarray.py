import math
n=int(input())
a=list(map(int,input().split()))
lis=[]
lis[:n+1]=[0]*(n+1)
for i in range(n):
    lis[i+1]=lis[i]+a[i]

cnt=0
for i in range(1,len(lis)):
    for j in range(i,len(lis)):
        cur_sum=lis[j]-lis[i-1]
        ps=math.sqrt(cur_sum)
        if(ps-math.floor(ps)==0):
            cnt+=1
print(cnt)