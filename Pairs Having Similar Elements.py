n=int(input())
a=list(map(int,input().split()))
cnt=0
list1,list2=[],[]
mat1,mat2=0,0
temp=0
a.sort()
print(a)
for i in range(n-1):
    if(a[i]-a[i+1]==1 or a[i+1]-a[i]==1):
        list1.append(i)
    elif(a[i]==a[i+1]):
        list2.append(i)
        