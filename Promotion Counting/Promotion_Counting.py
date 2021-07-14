file = open('promote.in')
list1 = [list(map(int,file.readline().split(' '))) for t in range(4)]
output = [0,0,0]
c = 0
for a in list1[1:]:
    subtracted = a[1]-a[0]
    output[c]+=subtracted
    c+=1
output[0],output[1] = output[1]+output[2]+output[0],output[1]+output[2]
file1 = open('promote.out','w')
for t in output:
    file1.write(str(t)+'\n')
