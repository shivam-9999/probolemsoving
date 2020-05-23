n=int(input())
for i in range(n):
    s1,s2=list(map(str,input())),list(map(str,input()))
    cnt=0
    for ch in s1:
        if ch in s2:
            cnt+=1
            indexs2=s2.index(ch)
            ch2=s2[indexs2]
            ch2=ch2.upper()
            s2[indexs2]=ch2
    print(len(s1)+len(s2)-cnt*2)

