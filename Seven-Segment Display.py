test=int(input())
for test in range(test):
    s=input()
    listInput=[]
    segment=[6,2,5,5,4,5,6,3,7,6]
    listInput.extend(s)
    n=len(listInput)
    sum=0
    for i in range(n):
        temp=listInput[i]
        sum+=segment[int(temp)]
    times=0
    if(sum%2==0):
        times=sum//2
        no = '1' * times
    else:
        times=(sum-3)//2
        no = '7'+'1' * times
    print(int(no))