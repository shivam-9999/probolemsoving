n=int(input())
A = [int(i) for i in input().split()]
product=1
for i in range(n):
    product=(product*A[i])%((10**9)+7)
print(product)


# list1=[]
# n=int(input())
# list1=list(map(int,input().split(" ")))
# # print(list1)
# ans=1
# for i in len(list1):
#     ans=(ans*list1[i])%((10**9)+7)
# print(ans)