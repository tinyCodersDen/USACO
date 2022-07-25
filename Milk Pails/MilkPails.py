file = open('pails.in','r')
I = list(map(int,file.readline().split(' ')))
ans = 0
for t in range(I[2]//I[0]):
    if (I[2]-((I[2]-((t+1)*I[0]))%I[1]))>ans: ans = (I[2]-((I[2]-((t+1)*I[0]))%I[1]))
writefile = open('pails.out','w')
writefile.write(str(ans))
