n,k = list(map(int, input().split()))
A = list(map(int, input().split()))
for i in range(n-k+1):
    print(max(A[i:i+k]),end=" ")