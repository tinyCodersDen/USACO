file = open('bcount.in','r')
writefile = open('bcount.out','a')
z = file.readline().split(' ')
dict1 = {1:[0]*int(int(z[0])+1),2:[0]*int(int(z[0])+1),3:[0]*int(int(z[0])+1)}
for t in range(1,int(z[0])+1):
    ask = file.readline()
    ask = ask.strip()
    ask=int(ask)
    if t>1:
        dict1[1][t]=dict1[1][t-1]
        dict1[2][t]=dict1[2][t-1]
        dict1[3][t]=dict1[3][t-1]
    dict1[ask][t]+=1

count1 = 0
for r in range(int(z[1])):
    ask = file.readline().split(' ')
    ask[0]=int(ask[0])
    ask[1]=int(ask[1])
    h = dict1[1][ask[1]] - dict1[1][ask[0]-1]
    g = dict1[2][ask[1]] - dict1[2][ask[0]-1]
    j = dict1[3][ask[1]] - dict1[3][ask[0]-1]
    print(h,g,j)
    string1 = str(h)+' '+str(g)+' '+str(j)
    count1+=1
    if count1<int(z[1]):
        writefile.write(string1+'\n')
    else:
        writefile.write(string1)
writefile.close()
file.close()
