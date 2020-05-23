t=int(input())
for testcase in range(t):
    a, b = list(map(int, input().split()))
    listA=list(map(int,input().split()))
    listB = list(map(int, input().split()))
    winValue=max(listB)+1
    ans=0
    for v in listA:
        if(v<winValue):
            t=winValue-v
            ans+=t*b
    print(ans)
