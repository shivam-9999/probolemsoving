# n=int(input())
# a=list(map(str,input().split()))
# nQ=int(input())
# for i in range(nQ):
#     l,r = list(map(int,input().split()))
#     finalLis=[]
#     l-=1
#     r-=1
#     cnt=0
#     ans=0
#     for j in range(l,r+1):
#         no1, no2= "", ""
#         for k in range(0,j):
#             no1+=a[k]
#         for l in range(j+1,len(a)):
#             no2 += a[l]
#         if (no1 == ""):
#             ans = int(no2)
#         elif(no2 == ""):
#             ans = int(no1)
#         else:
#             ans=int(no1)+int(no2)
#         if(ans%2==0 and ans%3==0 and ans%5==0):
#             finalLis.append(j)
#     print(len(finalLis))


n=int(input())
a=list(map(str,input().split()))
nQ=int(input())
x, y = [""] * n, [""] * n
for i in range(0, n):
    x[i] = x[i - 1] + a[i]
x.insert(0, 0)
print(x)
a = a[::-1]
for i in range(0, n):
    y[i] = a[i] + y[i - 1]
y = y[::-1]
y.pop(0)
y.append(0)
print(y)
for i in range(nQ):
    cnt=0
    l, r = list(map(int, input().split()))
    for j in range(l,r+1):
        ansL=int(x[j-1])+int(y[j-1])
        if (ansL % 2 == 0 and ansL % 3 == 0 and ansL % 5 == 0):
            cnt+=1
    print(cnt)