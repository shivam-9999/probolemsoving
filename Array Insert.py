aN,bN=list(map(int,input().split()))
a=list(map(int,input().split()))
x,y,z=[],[],[]
for i in range(aN):
    j,k,l=list(map(int,input().split()))
    x.append(j)
    y.append(k)
    z.append(l)
fList=[]
for i in range(bN):
    if(x[i]==1):
        a[y[i]]=z[i]
    else:
        fList.append(sum(a[y[i]:z[i]+1]))
for no in fList:
    print(no)


