N , Q = list(map(int , input().split()))
n = list(map(int , input().split()))
for i in range(Q):
    inp = list(map(int , input().split()))
    if(inp[0]==1):
        if(n[inp[1]-1]==0):
            n[inp[1]-1] = 1
        else:
            n[inp[1]-1] = 0
    else:
        if(n[inp[1]-1]==1):
            print("ODD")
        else:
            print("EVEN")
