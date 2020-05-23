s=list(map(str,input("")))
n=len(s)
mid=n//2
fHString,sHString="",""

if(n%2==0):
    fHList = s[:mid]
    sHList=s[n-1:mid-1:-1]
    for ele in fHList:
        fHString+=ele
    for ele in sHList:
        sHString+=ele
else:
    fHList = s[:mid]
    sHList = s[n-1:mid:-1]
    for ele in fHList:
        fHString += ele
    for ele in sHList:
        sHString += ele


# print(fHString,sHString)
if(fHString==sHString):
    print("Yes")
else:
    print("No")