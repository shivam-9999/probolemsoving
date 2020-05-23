# n=int(input())
# strlis=[]
# stage1Lis=[]
# stage2Lis=[]
# s=input()
# i=0
# for ch in s:
#     strlis.append(ch)
# while(i<n-1):
#     if(strlis[i]==strlis[i+1]):
#         i+=2
#     elif(strlis[i]!=strlis[i+1]):
#         stage1Lis.append(strlis[i])
#         i+=1
# stage1Lis.append(strlis[n-1])
# N=len(stage1Lis)
# j=0
# while(j<N-1):
#     if(stage1Lis[j]==stage1Lis[j+1]):
#         j+=2
#     elif (stage1Lis[j] != stage1Lis[j + 1]):
#         stage2Lis.append(stage1Lis[j])
#         j+=1
# stage2Lis.append(stage1Lis[N-1])
#
# ans=len(stage2Lis)
# str=""
# for ch in stage2Lis:
#     str+=ch
# print(ans)
# print(str)


n=int(input())
string=list(input())
stack=[]
for i in range(n):
    if len(stack)==0:
        stack.append(string[i])
    elif stack[-1]==string[i]:
        stack.pop(-1)
    else:
        stack.append(string[i])
print(len(stack))
print(''.join(stack))