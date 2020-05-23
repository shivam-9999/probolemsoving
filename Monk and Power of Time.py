n=int(input())
pA=list(map(int,input().split()))
pB=list(map(int,input().split()))
cnt=0
for i in range(n):
    if(pA[i]==pB[i]):
        pass
    while(pA[i]!=pB[i]):
        pA.append(pA[i])
        pA.remove(pA[i])
        cnt+=1
n=len(pA)
print(n+cnt)

