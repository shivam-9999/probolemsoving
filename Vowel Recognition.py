T=int(input())
for i in range(T):
    s=input()
    n=len(s)
    cnt=0
    for pos in range(n):
        if(s[pos]=='a' or s[pos]=='e' or s[pos]=='i' or s[pos]=='o' or s[pos]=='u' or s[pos]=='A' or s[pos]=='E'or s[pos]=='I'or s[pos]=='O' or s[pos]=='U'):
            cnt+=(n-l)*(l+1)
    print(cnt)