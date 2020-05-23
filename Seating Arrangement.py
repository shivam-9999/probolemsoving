n=int(input())
for i in range(n):
    sN=int(input(""))
    sNo=sN%12
    if(sNo==1):
        sN+=11
        print(sN,"WS")
    elif(sNo == 2):
        sN+=9
        print(sN,"MS")
    elif (sNo == 3):
        sN += 7
        print(sN,"AS")
    elif (sNo == 4):
        sN += 5
        print(sN,"AS")
    elif (sNo == 5):
        sN += 3
        print(sN,"MS")
    elif (sNo == 6):
        sN += 1
        print(sN,"WS")
    elif (sNo == 7):
        sN -= 1
        print(sN,"WS")
    elif (sNo == 8):
        sN -= 3
        print(sN,"MS")
    elif (sNo == 9):
        sN -= 5
        print(sN,"AS")
    elif (sNo == 10):
        sN -=7
        print(sN,"AS")
    elif (sNo == 11):
        sN -= 9
        print(sN,"MS")
    elif (sNo == 12 or sNo == 0):
        sN -= 11
        print(sN,"WS")