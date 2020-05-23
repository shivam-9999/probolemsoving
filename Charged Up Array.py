T=int(input())
for case in range(T):
    n=int(input())
    a=list(map(int,input().split()))
    subset = 2 ** (n - 1)
    ans = 0
    for i in range(n):
        if(a[i]>=subset):
            ans=(ans+a[i])%1000000007
    print(ans)