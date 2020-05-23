s=input()
cnt1,cnt2=0,0
for ch in s:
    if(ch=='z'):
        cnt1+=1
    if(ch=='o'):
        cnt2+=1

if(cnt1*2==cnt2):
    print("YES")
else:
    print("NO")