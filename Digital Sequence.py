# n=int(input())
# a=list(map(int,input().split()))
# lis=[]
# lis[:10]=[0]*(10)
# for i in range(n):
#     f0,f1,f2,f3,f4,f5,f6,f7,f8,f9=0,0,0,0,0,0,0,0,0,0
#     while(a[i]>0):
#         if(a[i]%10==0):
#             f0=1
#         elif (a[i] % 10 == 1):
#             f1 = 1
#         elif (a[i] % 10 == 2):
#             f2 = 1
#         elif (a[i] % 10 == 3):
#             f3 = 1
#         elif (a[i] % 10 == 4):
#             f4 = 1
#         elif (a[i] % 10 == 5):
#             f5 = 1
#         elif (a[i] % 10 == 6):
#             f6 = 1
#         elif (a[i] % 10 == 7):
#             f7 = 1
#         elif (a[i] % 10 == 8):
#             f8 = 1
#         else:
#             f9 = 1
#         a[i] //= 10
#     if(f0==1):
#         lis[0]+=1
#     if (f1 == 1):
#         lis[1] += 1
#     if (f2 == 1):
#         lis[2] += 1
#     if (f3 == 1):
#         lis[3] += 1
#     if (f4 == 1):
#         lis[4] += 1
#     if (f5 == 1):
#         lis[5] += 1
#     if (f6 ==1):
#         lis[6] += 1
#     if (f7 == 1):
#         lis[7] += 1
#     if (f8 == 1):
#         lis[8] += 1
#     if (f9 == 1):
#         lis[9] += 1
# print(max(lis))
