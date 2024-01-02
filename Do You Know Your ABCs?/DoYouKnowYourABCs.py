'''
Do You Know Your ABCs?
tinyCodersDen
USACO
2020 December Contest, Bronze
'''
ask = input("")
list1 = ask.split(' ')
list1 = [int(y) for y in list1]
list1.sort()
a,b = list1[0],list1[1]
for x in list1:
    if a+b in list1 and b+x in list1 and x+a in list1 and a+b+x in list1:
        c = x
print(a,b,c)
