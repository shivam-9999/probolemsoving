#python3
t,l=int(input()),list(map(int,input().split()))
l1=[]
n=sum(l)
for i in l:
    if ((n-i)%7)==0:
        a=i
        l1.append(i)

if len(l1)>0:
    print(l.index(min(l1)))
else:
    print("-1")
