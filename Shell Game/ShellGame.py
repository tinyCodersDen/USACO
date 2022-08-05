list1 = [1,2,3]
file = open('shell.in','r')
num = int(file.readline())
first,second,third = 0,0,0
for t in range(num):
    x = list(map(int,file.readline().split(' ')))
    list1[x[0]-1],list1[x[1]-1] = list1[x[1]-1],list1[x[0]-1]
    print(list1)
    if list1[x[-1]-1]==1:
        first+=1
    if list1[x[-1]-1]==2:
        second+=1
    if list1[x[-1]-1]==3:
        third+=1
file2 = open('shell.out','w')
file2.write(str(max(first,second,third)))
