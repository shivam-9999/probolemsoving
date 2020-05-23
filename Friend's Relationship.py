n=int(input())
for testCases in range(n):
    n=int(input())
    N=(n-1)*2
    for i in range(1,n+1):
        print(i*'*',end="")
        print(N*'#',end="")
        print(i*'*')
        N-=2