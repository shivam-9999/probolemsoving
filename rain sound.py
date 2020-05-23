import math as m
for _ in range(int(input())):
    l,r,s = map(int, input().split())
    if s>r or m.ceil(l/s) > m.floor(r/s):
        print('-1 -1')
    else:
        print(m.ceil(l/s), m.floor(r/s))