T=int(input())
for i in range(T):
    a,b=list(map(int,input().split()))
    if(a<b):
        rArea=a*b
        cArea=a*a
        n=rArea//cArea
    else:
        rArea = a * b
        cArea = b* b
        n = rArea // cArea
    print(n)