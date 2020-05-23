# n=int(input())
# list1=list(map(int,input().split()))
# list2=list(map(int,input().split()))
# cnt,t,n=0,0,len(list1)
# for i in range(n):
#     minV = min(list1)
#     for j in range(n):
#         if(list1[j]>minV):
#             list1[j]=list1[j]-list2[j]
#             cnt+=1
# print(cnt)

# def step():
#     n=int(input())
#     a=list(map(int,input().split()))
#     b=list(map(int,input().split()))
#     for x in range(min(a),-1,-1):
#         ok=True
#         ans=0
#         i=0
#         while(i<n and ok==True):
#             ok &= x==a[i] or b[i]>0 and a[i]%b[i]==x%b[i]
#             if(b[i]>0):
#                 ans+=(a[i]-x)//b[i]
#             i+=1
#         if(ok):
#             return print(ans)
#     print("-1")
# step()

