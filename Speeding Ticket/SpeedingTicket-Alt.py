#This is an alternate solution of the problem which doesn't require simulation and passes all test cases.
import sys

sys.stdin = open('speeding.in','r')
sys.stdout = open('speeding.out','w')

l = []
l2 = []
ans = 0
N,M = list(map(int,input('').split(' ')))
z = 0
for t in range(N):
    g = list(map(int,input('').split(' ')))
    z+=g[0]
    g[0] = z
    l.append(g)
z = 0
for y in range(M):
    f = list(map(int,input('').split(' ')))
    z+=f[0]
    f[0] = z
    l2.append(f)
l3 = []
for t in l:
    for j in l2:
        if t[0]<=j[0]:
            if t[0]!=j[0]:
                l3.append([t[0],j[1]])
                break
            break
for t in l3:
    l2.append(t)
for k in l2:
    for h in l:
        if k[0]<=h[0]:
            if k[1]>h[1] and k[1]-h[1]>ans:
                ans = k[1]-h[1]
                break
            break
print(ans)
