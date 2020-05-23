L,n=int(input()),int(input())
list1,list2=[],[]
for i in range(n):
    w,h = list(map(int, input().split()))
    list1.insert(i, w)
    list2.insert(i, h)
for i in range(n):
    if(list1[i]<L or list2[i]<L):
        print("UPLOAD ANOTHER")
    elif(list1[i]==L or list2[i]==L):
        print("ACCEPTED")
    else:
        print("CROP IT")