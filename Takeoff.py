Q = int(input())
while(Q):
    Q-=1
    n, p, q, r = [int(x) for x in input().split()]
    list=[]
    list[:n+1]=[0]*(n+1)
    c,cnt=0,0
    for i in range(p,n+1,p):
        list[i] += 1
    for j in range(q,n+1,q):
        list[j] += 1
    for k in range(r,n+1,r):
        list[k] += 1
    for no in list:
        if(no==1):
            cnt+=1
    print(cnt)