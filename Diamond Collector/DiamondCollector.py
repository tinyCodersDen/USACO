'''
Diamond Collector
tinyCodersDen
USACO
2016 US Open Contest, Bronze
'''
f = open('diamond.in','r')
N,k  = list(map(int,f.readline().split(' ')))
l = []
for t in range(N):
    l.append(int(f.readline()))
s = 0
for e,t in enumerate(l):
    c = 1
    for w,a in enumerate(l):
        if w!=e and abs(t-a)<=k and t<=a:
            c+=1
    if c>s:
        s = c
print(s)
w = open('diamond.out','w')
w.write(str(s))
