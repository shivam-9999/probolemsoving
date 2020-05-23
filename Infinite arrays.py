for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    stack=[]
    stack.append(A[0])
    for i in range(1,N):
        stack.append(stack[-1]+A[i])
    for x,y in zip(L,R):
        x-=2
        y-=1
        ans1=(x//N)*stack[-1]+stack[x%N]
        ans2=(y//N)*stack[-1]+stack[y%N]
        print((ans2-ans1)%1000000007)