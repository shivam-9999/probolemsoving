n=int(input())
a=list(map(int,input().split()))
a=a[::-1]
min=0
list=[]
for i in range(len(a)):
    if(min<a[i]):
        min=a[i]
    if(a[i]==min):
        list.append(a[i])

for j in range(len(list)-1,-1,-1):
    print(list[j],end=" ")

