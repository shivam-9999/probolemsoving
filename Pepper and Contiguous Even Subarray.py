T=int(input())
for cases in range(T):
    n=int(input())
    a = list(map(int,input().split()))
    min1 = 0
    t=False
    for i in range(n):
        cnt=0
        if((a[i]%2)!=0):
            continue
        elif((a[i]%2)==0):
            t |= True
            for j in range(i,n):
                if ((a[j] % 2) == 0):
                    cnt+=1
                else:
                    break
            min1=max(cnt,min1)
    if(t==True):
        print(min1)
    else:
        print("-1")

