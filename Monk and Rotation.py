# t=int(input())
# temp=[]
# for j in range(t):
#     n,k=map(int,input().split())
#     l=[x for x in input().split()]
#     rotate=k%n
#     l[-rotate:],l[rotate:]=l[:rotate],l[0:-rotate]
#     print(l)

t=int(input())
for j in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    k=k%n
    for i in range(n):
        print(l[(n-k+i)%n])