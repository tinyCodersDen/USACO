'''
Even More Odd Photos
tinyCodersDen
USACO
2021 January Contest, Bronze
'''
p = int(input(''))
ask = input('').split(' ')
even = 0
odd = 0
l = []
for y in ask:
    sum1 = int(y)/2
    if sum1==int(sum1):
        even+=1
    else:
        odd+=1
if odd==0 and even>0:
    print(1)
    exit()
if odd>0 and even==0:
    bool = False
    for q in range(p):
        if odd==1 and bool==True:
            l[-2]+=2
            odd-=1
            l.pop(-1)
            break
        else:
            if p!=sum(l):
                if len(l)==0:
                    l.append(2)
                    odd-=2
                    bool = False
                elif l[-1]==1:
                    l.append(2)
                    odd-=2
                    bool = False
                elif l[-1]==2:
                    l.append(1)
                    odd-=1
                    bool = True
    print(len(l))
    exit()
if even>odd:
    bool = False
    for q in range(p):
        if bool == False:
            l.append(2)
            even -=1
            bool = True
        elif bool == True:
            if odd == 0:
                break
            else:
                l.append(1)
                odd -=1
                bool = False
    print(len(l))
    exit()
if even==odd:
    print(even+odd)
    exit()
if odd>even:
    bool = False
    for q in range(p):
        if odd==1 and bool:
            l[-2]+=2
            odd-=1
            l.pop(-1)
            break
        else:
            if len(l)==0:
                l.append(2)
                even-=1
                bool = False
            elif l[-1]==1:
                l.append(2)
                if even!=0:
                    even-=1
                else:
                    odd-=2
                bool = False
            elif l[-1]==2:
                l.append(1)
                odd-=1
                bool = True
        if odd==0 and even==0:
            break
    print(len(l))
    exit()
