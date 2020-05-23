n=int(input())
for i in range(n):
    cnt=0
    N,rupess=list(map(int,input().split()))
    buildHeight=list(map(int, input().split()))
    stack=[]
    for i in range(0,N):
        if(len(stack)==0):
            stack.append(buildHeight[0])
        elif(stack[-1]<buildHeight[i]):
            stack.append(buildHeight[i])
    print(len(stack)*rupess)