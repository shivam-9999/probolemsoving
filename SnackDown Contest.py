T=int(input())
for cases in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    lis=[]
    lis[:101]=[0]*101
    cnt=0
    for i in range(1,a[0]+1):
        lis[a[i]]+=1
    for j in range(1,b[0]+1):
        lis[b[j]] += 1
    for k in range(len(lis)):
        if(lis[k]>0):
            cnt+=1
    if(n==cnt):
        print("YES")
    else:
        print("NO")


