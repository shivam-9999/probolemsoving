n=int(input())
list1,list2=[],[]
ansLis=[]
for i in range(n):
    a,b = list(map(int,input().split()))
    list1.append(a)
    list2.append(b)

zipped_pairs = zip(list1,list2)
pair = sorted(zipped_pairs)
max1=1000001
for p in pair:
    ansLis.append(p[0])
    ansLis.append(p[1])
ansLis.insert(0,0)
ansLis.append(max1)
ans=0
for j in range(0,len(ansLis),2):
    if(ansLis[j+1]-ansLis[j]>1):
        while((ansLis[j+1]-ansLis[j])>1):
            ans+=ansLis[j+1]-1
            ansLis[j + 1]+= - 1
print(ans)
