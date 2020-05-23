n=int(input())
a=list(map(str,input().split()))
listF=[]
if(len(a)%2==0):
    n=len(a)//2
else:
    n=len(a)//2+1
for i in range(n):
    temp,listB=0,[]
    temp=a[i]
    listB.extend(temp)
    listF.insert(i,str(listB[0]))

for j in range(n,len(a)):
    temp1=int(a[j])%10
    listF.insert(j,str(temp1))
fNo=""
for i in range(len(a)):
    fNo+=listF[i]
if(int(fNo)%11==0):
    print("OUI")
else:
    print("NON")