testCase=int(input())
for i in range(testCase):
    list1,list2=[],[]
    cnt1,cnt2=0,0
    cost1,cost2=list(map(int,input().split()))
    n=int(input())
    for i in range(n):
        dec1,dec2 = list(map(int,input().split()))
        list1.insert(i,dec1)
        list2.insert(i,dec2)
    for no1 in list1:
        if(no1==1):
            cnt1+=1
    for no2 in list2:
        if(no2==1):
            cnt2+=1
    if(cnt1<cnt2):
        if(cost1<cost2):
            print(cnt1*cost2+cnt2*cost1)
        else:
            print(cnt1*cost1+cnt2*cost2)
    else:
        if (cost1 < cost2):
            print(cnt1 * cost1 + cnt2 * cost2)
        else:
            print(cnt1 * cost2 + cnt2 * cost1)