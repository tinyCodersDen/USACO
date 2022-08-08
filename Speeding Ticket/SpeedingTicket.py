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
    l2.append(f)
y = 0
for k in l2:
    speed = k[1]
    for t in range(k[0]):
        y+=1
        for g in l:
            if g[0]>=y:
                if g[1]<speed and speed-g[1]>ans:
                    ans = speed-g[1]
                break
print(ans)
