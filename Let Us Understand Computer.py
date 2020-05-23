# T=int(input())
# for i in range(T):
#     n=int(input())
#     arr1 = []
#     t = 0
#     ans=0
#     for j in range(1,n+1):
#         n1,mainNo,subNo=n,0,0
#         temp = n1//j
#         while (temp > 0):
#             p = temp % 2
#             temp = temp // 2
#             if (p == 1):
#                 mainNo += 1
#         no=j
#         k=0
#         arr2=[]
#         while(no>0):
#             r=no%2
#             no=no//2
#             if(r==1):
#                 subNo+=1
#         if (mainNo <= subNo):
#             ans += 1
#     print(ans)

T=int(input())
for tCase in range(T):
    x=int(input())
    ans=0
    for i in range(1,x+1):
        if(bin(x//i)<=bin(i)):
            ans+=1
    print(ans)