n=int(input())
list1=[]
for i in range(n):
    subList=list(input())
    subList.sort()
    ok=True
    for i in range(1,len(subList)):
        if((int(subList[i-1])+1)==int(subList[i])):
            ok&=True
        else:
            ok&=False
    if(ok==True):
        print("YES")
    else:
        print("NO")

