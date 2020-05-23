# l,r,k=list(map(int,input().split()))
# cnt=0
# for i in range(l,r+1):
#     if((i%k)==0):
#         cnt+=1
# print(cnt)

# def fact(N):
#     if(N==1):
#         return N
#     else:
#         return N*fact(N-1)
#
# n = int(input())
# print(fact(n))

s=input()
for ch in s:
    if(ch.isupper()):
        ch=ch.lower()
    else:
        ch=ch.upper()
    print(ch,end="")