x = list(map(int,input('').split(' ')))
counts = list(map(int,input('').split(' ')))
counts.sort()
s = []
for t in range(x[0],0,-1):
    s.append(t)
h = 0
for e,t in enumerate(counts):
    if t>=s[e]:
        h=s[e]
        break
