n=int(input())
a=list(map(int,input().split()))
prev_sum=[]
prev_sum[:n+1]=[0]*(n+1)
for i in range(1,n+1):
    prev_sum[i]=prev_sum[i-1]+a[i-1]
cnt=0
ans=[]
N=0
for i in range(1,n+1):
    for j in range(i,n+1):
        cur_sum=prev_sum[j]-prev_sum[i-1]
        cur_no=j-i+1
        rem_sum=prev_sum[n]-cur_sum
        rem_no=n-cur_no
        cur_avg=cur_sum//cur_no
        if(rem_no==0):
            rem_avg=0
        else:
            rem_avg=(rem_sum // rem_no)
        if(cur_avg>rem_avg):
            ansIn=[]
            N+=1
            ansIn.append(i)
            ansIn.append(j)
            ans.append(ansIn)
print(N)
for x,y in sorted(ans):
    print(x,y)